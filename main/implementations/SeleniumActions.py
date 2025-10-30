from main.abstracts.IWebActions import IWebActions
from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumActions(IWebActions):
    """
    Implementation of IWebActions using selenium webdriver
    Element interactions occur in this class
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.default_timeout = 10
        self.wait = WebDriverWait(self.driver, self.default_timeout)

    def wait_until_visible(self, locator: Tuple, timeout: int = None) -> None:
        """Waits for an element to become visible """
        wait_time = timeout if timeout is not None else self.default_timeout
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(locator))

    def click(self, locator: Tuple) -> None:
        """Locates and clicks an element"""
        self.wait_until_visible(locator)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator: Tuple, text: str) -> None:
        """Locates and enters text into an element"""
        self.wait_until_visible(locator)
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: Tuple) -> str:
        """Locates and returns the text of an element"""
        self.wait_until_visible(locator)
        return self.driver.find_element(*locator).text

    def is_displayed(self, locator: Tuple) -> bool:
        """Locates and returns whether an element is displayed"""
        try:
            self.wait_until_visible(locator, timeout=5)
            return True
        except:
            return False


