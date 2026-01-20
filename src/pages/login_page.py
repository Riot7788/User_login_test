import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import BASE_URL

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    @allure.step("Открыть страницу логина")
    def open(self):
        self.driver.get(BASE_URL)

    @allure.step("Авторизоваться пользователем {username}")
    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Получить текст ошибки")
    def get_error_text(self):
        return self.find(self.ERROR_MESSAGE).text

    @allure.step("Проверить, что открыта страница каталога")
    def is_inventory_page_opened(self):
        return self.find(self.INVENTORY_CONTAINER).is_displayed()
