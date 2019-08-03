from base.basepage import BasePage
from utilities import custom_logger as cl
import logging,time

class RegisterAccount(BasePage):

    log = cl.customLogger(logLevel=logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    # locators
    _myAccounticon = "//span[contains(text(),'My Account')]"
    _register = "//ul[@class='dropdown-menu dropdown-menu-right']//a[contains(text(),'Register')]"
    # _register = "[class='dropdown-menu dropdown-menu-right']>li:first-child"
    _firstname = "input-firstname"
    _lastname = "input-lastname"
    _email = "input-email"
    _telephone = "input-telephone"
    _password = "input-password"
    _confirmpassword = "input-confirm"
    _newradiobtn = "//div[@class='form-group']//div[@class='col-sm-10']//label[1]"
    _agreecheckbox = "agree"
    _continuebtn = "//input[@class='btn btn-primary']"
    _successMsg = "//p[contains(text(),'Congratulations! Your new account has been success')]"

    # methods to perform action
    def clickRegisterAccount(self):
        self.elementClick(locator=self._myAccounticon,locatorType='xpath')
        time.sleep(2)
        self.elementClick(locator=self._register,locatorType='xpath')
    def enterPersonalDetails(self,FName,LName,Email,Teleophone):
        self.sendKeys(FName,locator=self._firstname)
        self.sendKeys(LName,locator=self._lastname)
        self.sendKeys(Email,locator=self._email)
        self.sendKeys(Teleophone,locator=self._telephone)
    def enterPassword(self,Password,ConfirmPassword):
        self.sendKeys(Password,locator=self._password)
        self.sendKeys(ConfirmPassword,locator=self._confirmpassword)
    def clickNewsLetterRadioButton(self):
        self.elementClick(locator=self._newradiobtn,locatorType='xpath')
    def clickAgreeCheckbox(self):
        self.elementClick(locator=self._agreecheckbox,locatorType='name')
    def clickContinue(self):
        self.elementClick(locator=self._continuebtn,locatorType='xpath')

    def registerAccount(self,FName,LName,Email,Teleophone,Password,ConfirmPassword):
        self.clickRegisterAccount()
        self.enterPersonalDetails(FName,LName,Email,Teleophone)
        self.enterPassword(Password,ConfirmPassword)
        self.clickNewsLetterRadioButton()
        self.clickAgreeCheckbox()
        self.clickContinue()

    def verifyaccountCreatedSuccessfully(self):
        messageElement = self.waitForElement(self._successMsg,locatorType='xpath')
        result = self.isElementDisplayed(element=messageElement)
        return result






