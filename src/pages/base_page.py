import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Найти элемент {locator}")
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        self.find(locator).click()

    @allure.step("Ввести текст '{text}' в поле {locator}")
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url