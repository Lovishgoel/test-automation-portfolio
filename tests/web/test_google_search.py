from playwright.sync_api import Page

def test_duckduckgo_search(page: Page):
    page.goto("https://duckduckgo.com/")
    page.fill("input[name='q']", "Materna Test Automation")
    page.press("input[name='q']", "Enter")
    page.wait_for_load_state("load")
    assert "Materna" in page.title()

