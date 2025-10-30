from abc import ABC, abstractmethod
from typing import Tuple

class IWebActions(ABC):
    """
    Interface for common browser interactions
    Locator is defined as a Tuple[B, str], eg By.ID, "username"
    """

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
    
    @abstractmethod
    def wait_until_visible(self, locator: Tuple, timeout: int = 10) -> None:
        """Waits until an element is visible"""
        pass