import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class SunscreenPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _cart_button = "#cart"
    _all_products = "//div[@class='text-center col-4']"
    _add_button = "//button[@class='btn btn-primary']"


    def clickaddButton(self):
        self.elementClick(self._add_button, locatorType="xpath")

    def addproduct(self):
        all_product = self.getElementList(self._all_products,locatorType="xpath")
        spf_30 = ""
        spf_50 = ""
        temp_list = []
        spf_30_price = 1000
        spf_50_price = 1000
        for i in all_product:
            if "spf-30" in i.text.lower():
                price = int((i.text.split("\n")[1]).split(" ")[-1])
                if price < spf_30_price:
                    spf_30 = i
                    spf_30_price = price
            elif "spf-50" in i.text.lower():
                price = int((i.text.split("\n")[1]).split(" ")[-1])
                if price < spf_50_price:
                    spf_50 = i
                    spf_50_price = price
        temp_list.append(spf_50)
        temp_list.append(spf_30)
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
        return self.verifyPageTitle("The Best Sunscreens in the World!")
