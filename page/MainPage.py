from  selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.__driver.current_url

    @allure.step("Открыть боковое меню")
    def open_menu(self):
        self.__driver.find_element(
            By.CSS_SELECTOR,'[data-testid="nav-profile-button--trigger"]').click()

    @allure.step("Прочитать информацию о пользователе")
    def get_account(self) -> list[str]:
        (WebDriverWait(self.__driver, 15).
         until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, '[data-testid="nav-profile-button--content--details"]'))))

       # Ищем имя пользователя
        name_element = self.__driver.find_element(
            By.CSS_SELECTOR, '[data-testid="nav-profile-button--content--details--name"]'
        )
        name = name_element.text

        # Ищем email пользователя
        email_element = self.__driver.find_element(
            By.CSS_SELECTOR, '[data-testid="nav-profile-button--content--details--email"]'
        )
        email = email_element.text

        return [name, email]