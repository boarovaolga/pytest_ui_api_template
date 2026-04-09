from  selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://id.atlassian.com/login"
        self.__driver = driver

    @allure.step("Перейти на страницу авторизации")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str):
        self.__driver.find_element(By.CSS_SELECTOR, "#username-uid1").send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.
                                                 CSS_SELECTOR, "svg[role=presentation]")))

        self.__driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

        WebDriverWait(self.__driver, 15).until(
            EC.url_contains("https://home.atlassian.com/"))
