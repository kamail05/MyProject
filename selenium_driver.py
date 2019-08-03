from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
from selenium.webdriver import ActionChains
import logging
import time
import os
import time
import traceback
from base.configreader import ConfigReader
from selenium import webdriver
import selenium.common.exceptions as e

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver


    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element
    def mousehovergetElement(self, svlocator, svlocatorType="id"):
        element = None
        try:
            svlocatorType = svlocatorType.lower()
            svbyType = self.getByType(svlocatorType)
            svelement = self.driver.find_element(svbyType, svlocator)
            self.log.info("Element found with locator: " + svlocator +
                          " and  locatorType: " + svlocatorType)
        except:
            self.log.info("Element not found with locator: " + svlocator +
                          " and  locatorType: " + svlocatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def mousehovermenuclick(self,driver,locator="",locatorType="id",svlocator="",svlocatorType="xpath"):
        try:
            self.driver = driver
            action = ActionChains(driver)
            firstLevelMenu = self.getElement(locator,locatorType)
            action.move_to_element(firstLevelMenu).perform()
            time.sleep(2)
            secondLevelMenu = self.mousehovergetElement(svlocator,svlocatorType)
            secondLevelMenu.click()
        except:
            print("Mouse Hover failed on element")

    def returnByType(self, locatorType):
        """
        Returns 'By' type of the locator provided

        Required Parameters:
            locatorType: Type of the locator(id(default), xpath, css, classname, linktext)

        Optional Parameters:
            None

        Returns:
            'By' type
        """
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.warning("Locator type " + locatorType + " not correct/supported")
            return False

    def waitForElement(self, locator, locatorType="id", info="", waitType="visible", timeout=10, pollFrequency=0.5):
        """
        Wait for element to present

        Required Parameters:
            locator: locator of the element to find

        Optional Parameters:
            locatorType: Type of the locator(id(default), xpath, css, classname, linktext)
            timeout: Maximum time you want to wait for the element
            pollFrequency: Frequency to poll for the element

        Returns:
            Boolean
        """
        startTime = int(round(time.time() * 1000))
        element = None
        try:
            byType = self.returnByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element '" + info + "' to be visible and clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            if waitType == "visible":
                element = wait.until(EC.visibility_of_element_located((byType, locator)))
            elif waitType == "clickable":
                element = wait.until(EC.element_to_be_clickable((byType, locator)))
            else:
                self.log.warning("WaitType not supported or incorrect")
            endTime = int(round(time.time() * 1000))
            duration = (endTime - startTime) / 1000.00
            self.log.info("Element '" + info +
                          "' appeared on the web page after :: " + "{0:.2f}".format(duration) + " :: seconds")
        except:
            self.log.error("Element '" + info +
                           "' not appeared on the web page after :: " + str(timeout) + " :: seconds")
        return element


    def clickElement(self, element, info, timeToWait=0):
        """
        Click Element

        Required Parameters:
            element: Element to click
            info: Information about the element, usually text on the element

        Optional Parameters:
            timeToWait: Time you want to wait after clicking the element

        Returns:
            boolean
        """
        if element is not None:
            try:
                element.click()
                self.log.info("clicked on element :: " + info)
                self.log.info("Waiting after clicking the element for "
                              + str(timeToWait) + " seconds")
                time.sleep(timeToWait)
                return True
            except:
                self.log.error("Failed to click element :: " +  info)
                traceback.print_stack()
                return False
        else:
            self.log.error("Element :: " + info +  " reference to none")
            return False

    def clickWhenReady(self, locator, locatorType="id", info="", timeout=10, pollFrequency=0.5, timeToWait=0):
        """
        Click Element when it's clickable

        Required Parameters:
            locator: locator of the element to find

        Optional Parameters:
            locatorType: Type of the locator(id(default), xpath, css, classname, linktext)
            info: Information about the element, usually text on the element
            timeout: Maximum time you want to wait for the element
            pollFrequency: Frequency to poll for the element
            timeToWait: Time you want to wait after clicking the element

        Returns:
            boolean
        """
        element = self.waitForElement(locator, locatorType=locatorType, waitType="clickable",
                                      timeout=timeout, pollFrequency=pollFrequency)
        self.clickElement(element, info, timeToWait=timeToWait)


    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def verifyElementTextContains(self, locator="",expectedText=""):
        """
        Check if the element contains the text

        Required Parameters:
            locator: Locator of the element
            expectedText: Text needs to be checked in element

        Optional Parameters:
            None

        Returns:
            Boolean
        """
        element = self.getElement(locator)
        actualText = element.text
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION CONTAINS !!!")
            return False

    def clearField(self, locator="", locatorType="id"):
        """
        Clear an element field
        """
        element = self.getElement(locator, locatorType)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locatorType: " + locatorType)

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed" )
            else:
                self.log.info("Element not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        """
        Check if element is present
        """
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + str(byType))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + str(byType))
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def webScroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    # def switchto(self):
