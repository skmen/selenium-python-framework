import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from main.pages.LoginPage import LoginPage

@pytest.fixture(scope="session")
def config():
    with open("config.json") as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(scope="function")
def driver(config):
    if config["test_environment"] == "browserstack":
        browserstack_user = config["browserstack_user"]
        browserstack_key = config["browserstack_key"]
        capabilities = config["browserstack_capabilities"]
        url = f"https://{browserstack_user}:{browserstack_key}@hub-cloud.browserstack.com/wd/hub"
        driver = webdriver.Remote(command_executor=url, desired_capabilities=capabilities)
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)
