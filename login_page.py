import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _myaccountMenu = "//span[contains(text(),'My Account')]"
    _login_link = "//ul[@class='dropdown-menu dropdown-menu-right']//a[contains(text(),'Login')]"
    _email_field = "input-email"
    _password_field = "input-password"
    _login_button = "//input[@class='btn btn-primary']"
    _myaccount = "//span[contains(text(),'My Account')]"
    _logout = "//ul[@class='dropdown-menu dropdown-menu-right']//a[contains(text(),'Logout')]"

    def clickMyAccountMenu(self):
        self.elementClick(locator=self._myaccountMenu,locatorType="xpath")

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickMyAccountMenu()
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(2)

    def verifyLoginSuccessful(self):
        self.waitForElement("//h2[contains(text(),'My Account')]",
                                       locatorType="xpath")
        result = self.isElementPresent(locator="//h2[contains(text(),'My Account')]",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator="//div[@class='alert alert-danger alert-dismissible']",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("The Ninja Store")

    def logout(self):
        self.elementClick(locator=self._myaccount,locatorType="xpath")
        logoutLinkElement = self.waitForElement(locator=self._logout,
                          locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)
        # self.elementClick(locator="//div[@id='navbar']//a[@href='/sign_out']",
        #                   locatorType="xpath")

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()
