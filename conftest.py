import pytest
from playwright.sync_api import sync_playwright
import os
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        yield page
        context.close()
        browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook runs after each test
    outcome = yield
    rep = outcome.get_result()
    # Only act on test failures
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            page_name = item.name
            screenshot_path = os.path.join("screenshots", f"{page_name}.png")
            page.screenshot(path = screenshot_path)
            print(f"\n screenshot saved to {screenshot_path}")






