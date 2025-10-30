# conftest.py

import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from main.implementations.SeleniumActions import SeleniumActions
from main.pages.LoginPage import LoginPage
from main.abstracts.ILoginPage import ILoginPage

# --- Fixture 1: Configuration Loader ---
@pytest.fixture(scope="session")
def config():
    """Reads and returns the content of config.json."""
    with open('config.json') as f:
        return json.load(f)

# --- Fixture 2: WebDriver Manager (Local or Remote) ---
@pytest.fixture(scope="function")
def browser(config):
    """
    A fixture that sets up and tears down the WebDriver instance, 
    supporting both local and BrowserStack execution.
    """
    
    environment = config.get("test_environment", "local")
    driver = None
    
    if environment == "local":
        print("\nStarting local Chrome browser...")
        # Setup for LOCAL execution
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        
    elif environment == "browserstack":
        print("\nConnecting to BrowserStack remote WebDriver...")
        
        # 1. Get credentials
        bs_user = config["browserstack_user"]
        bs_key = config["browserstack_key"]
        
        # 2. Set up the Remote URL
        remote_url = f"https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub"
        
        # 3. Configure capabilities (Using the standardized Options object)
        bstack_capabilities = config["browserstack_capabilities"]
        
        # We need an Options object to pass capabilities in Selenium 4+
        # Using a generic Options object as we don't have a specific browser class imported
        options = Options() # We will use ChromeOptions as an example
        
        # Convert BrowserStack options into the format expected by Selenium 4
        # Note: We must unpack bstack:options into the options object, and then set browser name/version
        
        bstack_options = bstack_capabilities.pop("bstack:options", {})
        options.browser_name = bstack_capabilities.get("browserName", "chrome")
        options.browser_version = bstack_capabilities.get("browserVersion", "latest")

        # Set BrowserStack specific options using the standardized prefix
        options.set_capability("bstack:options", bstack_options)

        # 4. Initialize the Remote WebDriver using the 'options' argument
        driver = webdriver.Remote(
            command_executor=remote_url,
            options=options # Use 'options' instead of 'desired_capabilities'
        )
        
    else:
        raise ValueError(f"Unknown test_environment: {environment}. Must be 'local' or 'browserstack'.")

    # Common driver settings
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    # Run the test
    yield driver
    
    # Teardown: Close the browser after the test is complete
    driver.quit()

# --- Fixture 3: Web Actions Injector (Concrete Implementation) ---
@pytest.fixture(scope="function")
def actions(browser):
    """
    Dependency Injection Fixture: Returns the IWebActions interface,
    implemented by the SeleniumActions concrete class, injected with the driver.
    """
    # Note: SeleniumActions is imported at the top of the file
    return SeleniumActions(browser) 

# --- Fixture 4: Login Page Injector (Concrete Implementation) ---
@pytest.fixture(scope="function")
def login_page(actions): 
    """
    Dependency Injection Fixture: Returns the ILoginPage interface,
    implemented by the SeleniumLoginPage concrete class, injected with IWebActions.
    """
    # Note: SeleniumLoginPage is imported at the top of the file
    return LoginPage(actions)