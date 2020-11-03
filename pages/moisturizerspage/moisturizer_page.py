import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class MoisturizerPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _cart_button = "#cart"
    _all_products = "//div[@class='text-center col-4']"
    _add_button = "//button[@class='btn btn-primary']"
    _info_button = "//span[@class='octicon octicon-info']"

    def clickaddButtonsingle(self):
        self.elementClick(self._add_button, locatorType="xpath")

    def addproduct(self):
        all_product = self.getElementList(self._all_products,locatorType="xpath")
        aloe = ""
        almond = ""
        temp_list = []
        aloe_price = 1000
        almond_price = 1000
        for i in all_product:
            if "aloe" in i.text.lower():
                price = int((i.text.split("\n")[1]).split(" ")[-1])
                if price < aloe_price:
                    aloe = i
                    aloe_price = price
            elif "almond" in i.text.lower():
                price = int((i.text.split("\n")[1]).split(" ")[-1])
                if price < almond_price:
                    almond = i
                    almond_price = price
        temp_list.append(aloe)
        temp_list.append(almond)
        if len(temp_list) > 0:
            for j in temp_list:
                j.location_once_scrolled_into_view
                print(j.text)
                j.find_element_by_xpath(".//button[contains(text (),'Add')]").click()

    def cartstatus(self):
        temp = self.getText(self._cart_button, locatorType="css")
        return temp.lower()

    def clickcartButton(self):
        self.elementClick(self._cart_button, locatorType="css")

    def sunscreenPageTitle(self):
        return self.verifyPageTitle("The Best Moisturizers in the World!")