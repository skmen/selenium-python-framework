#abstracts/BasePage.py

from abc import ABC, abstractmethod

class IBaseWebPage(ABC):
    """
    Interface/base page for all pages of the automation demo site
    """

    @abstractmethod
    def load(self, url: str) -> None:
        """Navigates the browser to the specificed URL"""
        pass

    @abstractmethod
    def get_page_title(self) -> str:
        """Returns the page title"""
        pass