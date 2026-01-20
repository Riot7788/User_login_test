import allure
from pages.login_page import LoginPage
from config import (
    STANDARD_USER, STANDARD_PASSWORD,
    LOCKED_USER, PERFORMANCE_USER,
    WRONG_PASSWORD
)

@allure.feature("Авторизация")
@allure.story("Открытие страницы логина")
def test_open_site(driver):
    """Тест открытие страницы"""
    page = LoginPage(driver)
    page.open()
    assert "saucedemo" in page.get_current_url()

@allure.feature("Авторизация")
@allure.story("Успешный логин standard_user")
def test_successful_login(driver):
    """Тест успешный логин standard_user"""
    page = LoginPage(driver)
    page.open()
    page.login(STANDARD_USER, STANDARD_PASSWORD)
    assert "inventory.html" in page.get_current_url()
    assert page.is_inventory_page_opened()

@allure.feature("Авторизация")
@allure.story("Логин с неверным паролем")
def test_login_wrong_password(driver):
    """Логин с неверным паролем"""
    page = LoginPage(driver)
    page.open()
    page.login(STANDARD_USER, WRONG_PASSWORD)
    assert "Epic sadface" in page.get_error_text()

@allure.feature("Авторизация")
@allure.story("Логин заблокированного пользователя")
def test_locked_user(driver):
    """Логин заблокированного пользователя"""
    page = LoginPage(driver)
    page.open()
    page.login(LOCKED_USER, STANDARD_PASSWORD)
    assert "locked out" in page.get_error_text()

@allure.feature("Авторизация")
@allure.story("Логин с пустыми полями")
def test_empty_fields(driver):
    """Логин с пустыми полями"""
    page = LoginPage(driver)
    page.open()
    page.login("", "")
    assert "Username is required" in page.get_error_text()

@allure.feature("Авторизация")
@allure.story("Логин пользователем PERFORMANCE_USER")
def test_login_performance_user(driver):
    """Логин пользователем PERFORMANCE_USER"""
    page = LoginPage(driver)
    page.open()
    page.login(PERFORMANCE_USER, STANDARD_PASSWORD)
    assert "inventory.html" in page.get_current_url()
    assert page.is_inventory_page_opened()

@allure.feature("Авторизация")
@allure.story("Логин с пустым паролем")
def test_empty_password(driver):
    """Логин с пустым паролем"""
    page = LoginPage(driver)
    page.open()
    page.login(STANDARD_USER, "")
    assert "Password is required" in page.get_error_text()

@allure.feature("Авторизация")
@allure.story("Логин с пустым username")
def test_empty_username(driver):
    page = LoginPage(driver)
    page.open()
    page.login("", STANDARD_PASSWORD)
    assert "Username is required" in page.get_error_text()
