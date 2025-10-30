from abc import ABC, abstractmethod
from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver

class IWebActions(ABC):
    """
    Interface for web browser actions
    """

    @abstractmethod
    def wait_until_visible(self, locator: Tuple, timeout: int = None) -> None:
        """Waits for an element to become visible """
        pass

    @abstractmethod
    def click(self, locator: Tuple) -> None:
        """Locates and clicks an element"""
        pass

    @abstractmethod
    def enter_text(self, locator: Tuple, text: str) -> None:
        """Locates and enters text into an element"""
        pass

    @abstractmethod
    def get_text(self, locator: Tuple) -> str:
        """Locates and returns the text of an element"""
        pass

    @abstractmethod
    def is_displayed(self, locator: Tuple) -> bool:
        """Locates and returns whether an element is displayed"""
        pass
