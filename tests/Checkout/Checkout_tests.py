from pages.sunscreenpage.sun_screen_page import SunscreenPage
from pages.homepage.home_page import HomePage
from pages.moisturizerspage.moisturizer_page import MoisturizerPage
from pages.checkoutpage.checkout_page import CheckoutPage
from utilities.test_status import Status
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time


@pytest.mark.usefixtures("oneTimeSetUp")
class CheckoutFlowTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ssp = SunscreenPage(self.driver)
        self.mp = MoisturizerPage(self.driver)
        self.cp = CheckoutPage(self.driver)
        self.ts = Status(self.driver)


    # @pytest.mark.run(order=2)
    def test_t1CheckoutFlow(self):
        self.log.info("test_t1CheckoutFlow started")
        home_page_title_result = self.hp.homePageTitle()
        self.ts.mark(home_page_title_result,"home Page Verification")
        temperature = self.hp.getTemperature()
        if int(temperature) > 34:
            self.hp.sunscreenButton()
            self.ssp.addproduct()
            self.ssp.clickcartButton()
            self.cp.clickPayButton()
            self.cp.switchIframe()
            self.cp.stripeEnterDetails("amitmech17@gmail.com","4242424242424242","987","08/22","281001")
            time.sleep(10)
            self.cp.switchDefault()
        elif int(temperature) < 19:
            self.hp.moisturizersButton()
            self.mp.addproduct()
            self.mp.clickcartButton()
            self.cp.clickPayButton()
            self.cp.switchIframe()
            self.cp.stripeEnterDetails("amitmech17@gmail.com","4242424242424242","987","08/22","281001")
            time.sleep(10)
            self.cp.switchDefault()
        checkout_success_result = self.cp.paymentSuccessStatus()
        self.ts.markFinal("test_t1CheckoutFlow",checkout_success_result,"Checkout Flow is completed")