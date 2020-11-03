import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class CheckoutPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _total_amount = "#total"
    _card_pay_button = "//button[@class='stripe-button-el']"
    _i_frame = "stripe_checkout_app"
    _stripe_email_input_field = "//input[@placeholder='Email']"
    _stripe_card_number_input_field = "//input[@placeholder='Card number']"
    _stripe_month_input_field = "//input[@placeholder='MM / YY']"
    _stripe_cvv_input_field = "//input[@placeholder='CVC']"
    _stripe_zip_code_input_field = "//input[@placeholder='ZIP Code']"
    _stripe_pay_button = "//button[@type='submit']"
    _success_tag = "h2"


    def clickPayButton(self):
        self.elementClick(self._card_pay_button, locatorType="xpath")

    def totalAmount(self):
        return self.getText(self._total_amount, locatorType="css")

    def checkoutPageTitle(self):
        return self.verifyPageTitle("Cart Items")

    def switchIframe(self):
        iframe = self.getElement(self._i_frame,locatorType="name")
        self.switchToFrame(iframe)

    def switchDefault(self):
        self.switchToDefault()

    def stripeEnterDetails(self,email,cardnumber,cvv,month,zip):
        self.sendKeys(email,self._stripe_email_input_field,locatorType="xpath")
        self.sendKeys(cardnumber, self._stripe_card_number_input_field, locatorType="xpath")
        self.sendKeys(cvv, self._stripe_cvv_input_field, locatorType="xpath")
        self.sendKeys(month, self._stripe_month_input_field, locatorType="xpath")
        self.sendKeys(zip, self._stripe_zip_code_input_field, locatorType="xpath")
        self.elementClick(self._stripe_pay_button,locatorType="xpath")

    def paymentSuccessStatus(self):
        if self.getText(self._success_tag,locatorType="tag") == "PAYMENT SUCCESS":
            return True
        else:
            return False