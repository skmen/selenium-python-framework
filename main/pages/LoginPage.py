from selenium.webdriver.remote.webdriver import WebDriver
from main.abstracts.ILoginPage import ILoginPage
from main.implementations.SeleniumActions import SeleniumActions
from selenium.webdriver.common.by import By

class LoginPage(ILoginPage):
    """
    Implementation of the login page
    """

    def __init__(self, driver: WebDriver):
        self.actions = SeleniumActions(driver)

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    SUCCESS_MESSAGE = (By.ID, "success")
    ERROR_MESSAGE = (By.ID, "error")

    def login(self, username: str, password: str) -> None:
        """Logs in to the automation demo site"""
        self.actions.enter_text(self.USERNAME_INPUT, username)
        self.actions.enter_text(self.PASSWORD_INPUT, password)
        self.actions.click(self.LOGIN_BUTTON)

    def get_success_message_text(self) -> str:
        """Returns the text of the success message"""
        return self.actions.get_text(self.SUCCESS_MESSAGE)

    def get_error_message_text(self) -> str:
        """Returns the text of the error message"""
        return self.actions.get_text(self.ERROR_MESSAGE)
