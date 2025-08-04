from playwright.sync_api import Page
def test_login_form(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("input#username", "tomsmith")
    page.fill("input#password", "SuperSecretPassword!")
    page.click("button[type = 'submit']")
    page.wait_for_selector(".flash.success")
    assert "You logged into a secure area!" in page.inner_text(".flash.success")