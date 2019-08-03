from base.basepage import BasePage
from utilities import custom_logger as cl
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import os
import time
import subprocess

class AppleOrder(BasePage):

    log = cl.customLogger(logLevel=logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    # locators
    _home = "//a[contains(text(),'The Ninja Store')]"
    _desktoplink = "//li[contains(@class,'dropdown')]/a[contains(text(),'Desktops')]"
    _showalldesktop = "//a[contains(text(),'Show All Desktops')]"
    _applecinema = "//div[@id='content']//div[1]//div[1]//div[1]//a[1]//img[1]"
    _addtocart = "//div[@id='content']//div[1]//div[1]//div[2]//div[2]//button[1]"
    _radiobtn = "//div[@id='input-option218']//div[2]//label[1]"
    _checkbox = "//div[@id='input-option223']//div[2]//label[1]"
    _textfield = "input-option208"
    _dropdown = "//select[@id='input-option217']"
    _textarea = "input-option209"
    _fileupload = "button-upload222"
    _datefield = "//div[@class='input-group date']//button[@class='btn btn-default']"
    _date = "((//div[@class='datepicker'])[1])/div[1]/table/tbody/tr[4]/td[2]"
    _timefield = "//div[@class='input-group time']//button[@class='btn btn-default']"
    _time = "(//a[@data-action='incrementHours'])[2]"
    _dateandtimefield = "//div[@class='input-group datetime']//button[@class='btn btn-default']"
    _date_time = "(//table[@class='table-condensed'])[4]/tbody/tr[4]/td[4]"
    _timeabtn = "//li[@class='picker-switch accordion-toggle']//a[@class='btn']"
    _time_date = "(//a[@data-action='incrementHours'])[1]"
    _addcart = "//button[@id='button-cart']"
    _successmsg = "//div[@class='alert alert-success alert-dismissible']"

    # Functions/Methods to perform action

    def clickShowAllDesktop(self):
        mainmenu = self.getElement(locator=self._desktoplink,locatorType='xpath')
        action = ActionChains(self.driver)
        action.move_to_element(mainmenu).perform()
        submenu = self.getElement(locator=self._showalldesktop,locatorType="xpath")
        action.move_to_element(submenu).click().perform()

    def clickAppleDesktop(self):
        self.elementClick(locator=self._applecinema,locatorType='xpath')

    def clickradiobtn(self):
        self.elementClick(locator=self._radiobtn,locatorType="xpath")

    def selectcheckbox(self):
        self.elementClick(locator=self._checkbox,locatorType='xpath')

    def entertext(self):
        self.sendKeys('Test123',locator=self._textfield,locatorType='id')

    def selectdropdown(self):
        # dropdownelem = self.getElement(locator=self._dropdown,locatorType='xpath')
        a = Select(self.getElement(locator=self._dropdown,locatorType='xpath'))
        a.select_by_value('1')

    def sendKeyToTextArea(self):
        self.sendKeys('Testing Automation jly06',locator=self._textarea)

    def fileupload(self):
        file_input = self.driver.find_element_by_id(self._fileupload)
        # time.sleep(2)
        file_input.click()
        # subprocess.call("D:\workspace selenium\AutoIT\FileUploadScript.exe")
        # cmd = "D:\workspace selenium\AutoIT\FileUploadScript.exe"
        # process = subprocess.Popen(cmd, stdout=subprocess.PIPE, creationflags=0x08000000)
        # process.wait()
        # subprocess.Popen("D:\workspace selenium\AutoIT\FileUploadScript.exe", stdout=subprocess.PIPE,
        #                  stderr=subprocess.PIPE,shell=True).communicate()
        # os.system("D:\workspace selenium\AutoIT\FileUploadScript.exe")
        os.startfile("D:\workspace selenium\AutoIT\FileUploadScript.exe")
        time.sleep(10)
        fileuploadalert = self.driver.switch_to.alert
        fileuploadalert.accept()

    def selectDate(self):
        self.elementClick(locator=self._datefield,locatorType='xpath')
        time.sleep(3)
        self.elementClick(locator=self._date,locatorType='xpath')

    def settime(self):
        self.elementClick(locator=self._timefield,locatorType='xpath')
        time.sleep(10)
        self.elementClick(locator=self._time,locatorType='xpath')
        self.elementClick(locator=self._timefield,locatorType='xpath')

    def setdateandtime(self):
        self.elementClick(locator=self._dateandtimefield,locatorType='xpath')
        self.elementClick(locator=self._date_time,locatorType='xpath')
        time.sleep(2)
        self.elementClick(locator=self._timeabtn,locatorType='xpath')
        self.elementClick(locator=self._time_date,locatorType='xpath')

    def clickaddtocart(self):
        self.elementClick(locator=self._addcart,locatorType='xpath')

    def verifyapplesuccessfully(self):
        # result = self.verifyPageTitle("Success: You have added Apple Cinema 30 to your shopping cart!")
        result = self.isElementDisplayed(locator="//div[@class='alert alert-success alert-dismissible']",locatorType="xpath")
        return result

    def orderapple(self):
        self.clickShowAllDesktop()
        self.clickAppleDesktop()
        self.clickradiobtn()
        self.selectcheckbox()
        self.entertext()
        self.selectdropdown()
        self.sendKeyToTextArea()
        self.fileupload()
        self.selectDate()
        self.settime()
        self.setdateandtime()
        self.clickaddtocart()








