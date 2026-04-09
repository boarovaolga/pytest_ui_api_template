from  selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    def get_current_url(self):
        return self.__driver.current_url

    def open_menu(self):
        self.__driver.find_element(
            By.CSS_SELECTOR,'[data-testid="nav-profile-button--trigger"]').click()

    # Получить информацию о пользователе:
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