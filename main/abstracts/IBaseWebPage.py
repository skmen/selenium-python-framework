from abc import ABC, abstractmethod
from main.abstracts.IWebActions import IWebActions

class IBaseWebPage(ABC):
    """
    Base interface for all web pages
    """

    @property
    @abstractmethod
    def actions(self) -> IWebActions:
        """Returns the web actions implementation"""
        pass
