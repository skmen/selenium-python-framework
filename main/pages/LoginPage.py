#main/pages/LoginPage.py

from selenium.webdriver.common.by import By
from main.abstracts.ILoginPage import ILoginPage
from main.implementations.IWebActions import IWebActions

class LoginPage:
    """
    POM for the Login page of the automation demo site
    """

    URL = "https://skmen.github.io/automation-demo-site/login.html"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.NAME, "login")
    SUCCESS_NAVIGATOR = (By.TAG_NAME, "h1")
    ERROR_MESSAGE = (By.ID, "error-message")


    #initialize the page withe the IWebActions interface
    def __init__(self, actions: IWebActions):
        self.actions = actions


    def load(self, url: str = URL) -> None:
        """Navigates the browser to the login page"""
        self.actions.driver.get(url)

    def get_page_title(self) -> str:
        """Returns the page title"""
        return self.actions.driver.title

    def login(self, username: str, password: str) -> None:
        """Logs in to the automation demo site"""  
        self.actions.enter_text(self.USERNAME_INPUT, username)
        self.actions.enter_text(self.PASSWORD_INPUT, password)
        self.actions.click(self.LOGIN_BUTTON)

    def get_success_message_text(self) -> str:
        """Returns the text of the success message"""
        return self.actions.get_text(self.SUCCESS_NAVIGATOR)

    def get_error_message_text(self) -> str:
        """Returns the text of the error message"""
        return self.actions.get_text(self.ERROR_MESSAGE)

