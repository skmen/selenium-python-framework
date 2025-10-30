# main/abstracts/ILoginPage.py

from main.abstracts.IBaseWebPage import IBaseWebPage
from abc import abstractmethod

class ILoginPage(IBaseWebPage):
    """
    Interface for login functionality. Inherits from IBaseWebPage
    """

    @abstractmethod
    def login(self, username: str, password: str) -> None:
        """Logs in to the automation demo site"""
        pass

    @abstractmethod
    def get_success_message_text(self) -> str:
        """Returns the text of the success message"""
        pass

    @abstractmethod
    def get_error_message_text(self) -> str:
        """Returns the text of the error message"""
        pass