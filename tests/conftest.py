import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = "https://demoqa.com"
    browser.config.timeout = 6.0
    browser.config.window_height = 1366
    browser.config.window_width = 1024
    browser.config.driver_name = "firefox"

    yield
    browser.quit()
