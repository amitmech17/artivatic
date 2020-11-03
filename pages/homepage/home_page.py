import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class HomePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _temperature_field = "#temperature"
    _moisturizers_button = "//a[@href='/moisturizer']"
    _sunscreens_button = "//a[@href='/sunscreen']"


    def getTemperature(self):
        temp = self.getText(self._temperature_field, locatorType="css")
        return temp.split(" ")[0]

    def sunscreenButton(self):
        self.elementClick(self._sunscreens_button, locatorType="xpath")

    def moisturizersButton(self):
        self.elementClick(self._moisturizers_button, locatorType="xpath")

    def homePageTitle(self):
        return self.verifyPageTitle("Current Temperature")