import time
from pages.login_page import LoginPage


def test_open_site(driver):
    page = LoginPage(driver)
    page.open()
    time.sleep(4)
    assert "saucedemo" in page.get_current_url()