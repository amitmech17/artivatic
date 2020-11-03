"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie(IEDriverManager().install())
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif self.browser == "edge":
            driver = webdriver.Firefox(executable_path=EdgeChromiumDriverManager().install())
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.set_window_size(1440, 900)
        else:
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        return driver
