import pytest
@pytest.mark.parametrize("username, password, expected_message, is_success", [("tomsmith", "SuperSecretPassword!", "You logged into a secure area!", True),("lovi", "kol", "Your username is invalid!", False), ("tomsmith", "pass", "Your password is invalid!", False)])
def test_login_page(page, username, password, expected_message, is_success):
    page.fill("input#username", username)
    page.fill("input#password", password)
    page.click("button[type = 'submit']")
    flash = page.wait_for_selector("div.flash")
    message = flash.inner_text()
    assert expected_message in message.strip()
    if is_success:
        assert "/secure" in page.url

    else:
        assert "/login" in page.url



                                                                               