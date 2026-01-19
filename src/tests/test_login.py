import time
from pages.login_page import LoginPage
from config import (
    STANDARD_USER, STANDARD_PASSWORD,
    LOCKED_USER, PERFORMANCE_USER,
    WRONG_PASSWORD
)


def test_open_site(driver):
    """Тест открытие страницы"""
    page = LoginPage(driver)
    page.open()
    time.sleep(2)
    assert "saucedemo" in page.get_current_url()


def test_successful_login(driver):
    """Тест успешный логин standard_user"""
    page = LoginPage(driver)
    page.open()
    page.login(STANDARD_USER, STANDARD_PASSWORD)
    assert "inventory.html" in page.get_current_url()
    assert page.is_inventory_page_opened()


def test_login_wrong_password(driver):
    """Логин с неверным паролем"""
    page = LoginPage(driver)
    page.open()
    page.login(STANDARD_USER, WRONG_PASSWORD)
    assert "Epic sadface" in page.get_error_text()


def test_locked_user(driver):
    """Логин заблокированного пользователя"""
    page = LoginPage(driver)
    page.open()
    page.login(LOCKED_USER, STANDARD_PASSWORD)
    assert "locked out" in page.get_error_text()


def test_empty_fields(driver):
    """Логин с пустыми полями"""
    page = LoginPage(driver)
    page.open()
    page.login("", "")
    assert "Username is required" in page.get_error_text()


def test_login_performance_user(driver):
    """Логин пользователем PERFORMANCE_USER"""
    page = LoginPage(driver)
    page.open()
    page.login(PERFORMANCE_USER, STANDARD_PASSWORD)
    assert "inventory.html" in page.get_current_url()
    assert page.is_inventory_page_opened()