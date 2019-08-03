from base.basepage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from utilities import custom_logger as cl
from selenium.webdriver.common.by import By
import logging
import time

class DesktopOrder(BasePage):

    log = cl.customLogger(logLevel=logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    # locators
    _home = "//a[contains(text(),'The Ninja Store')]"
    _desktoplink = "//li[contains(@class,'dropdown')]/a[contains(text(),'Desktops')]"
    _showalldesktop = "//a[contains(text(),'Show All Desktops')]"
    _listview = 'list-view'
    _sortby = 'input-sort'
    _sortbyoption = "//option[contains(text(),'Rating (Highest)')]"
    _addtocart = "//div[@id='content']//div[1]//div[1]//div[2]//div[2]//button[1]"
    _addedtocardsuccessmsg = "//div[@class='alert alert-success alert-dismissible']"
    # CHECKOUT - Options
    _cart = "//span[@id='cart-total']"
    _viewCart = "//strong[contains(text(),'View Cart')]"
    _quantity = "//input[@name='quantity[3343]']"
    _quantityUpdate = "//span[@class='input-group-btn']//button[@class='btn btn-primary']"
    _estimateShippingandTaxes = "//a[contains(text(),'Estimate Shipping & Taxes')]"
    _TaxCountry = "input-country"
    _TaxState = "input-zone"
    _Taxpostalcode = "input-postcode"
    _getQuotes = "button-quote"
    _shippingmethod = "//label[contains(text(),'Flat Shipping Rate - $5.00')]"
    _applyshipping = "button-shipping"
    _checkOut = "//a[@class='btn btn-primary']"
    _verifyorder = "//a[contains(text(),'Success')]"

    # CHECKOUT - Billing Details
    _addnewaddress = "//div[3]//label[1]//input[1]"
    _Billingfirstname = 'input-payment-firstname'
    _Billinglastname = 'input-payment-lastname'
    _BillingAddress1 = 'input-payment-address-1'
    _BillingcCity = 'input-payment-city'
    _BillingPostaCode = 'input-payment-postcode'
    _BillingCountry = 'input-payment-country'
    _BillingState = 'input-payment-zone'
    _Billingcontinue = 'button-shipping-address'
    _paymentaddressbutton = "//input[@id='button-payment-address']"

    # DELIVERY DETAILS
    _continueShippingAddress = 'button-shipping-address'

    # DELIVERYMETHOD
    _comment = 'comment'
    _deliverymethodContinue = 'button-shipping-method'

    # PAYMENTMETHOD
    _agreecheckbox = 'agree'
    _PaymentMethodContinue = 'button-payment-method'

    # CONFIRMORDER
    _confirmorderButton = 'button-confirm'
    _ConfirmbtnforAsset = 'btn btn-primary'

    # methods to perform action
    def clickShowAllDesktop(self):
        element = self.driver.find_element(By.XPATH, self._desktoplink)
        itemToClickLocator = self._showalldesktop
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.log.info("Mouse Hovered on element ",element)
            time.sleep(2)
            topLink = self.driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(topLink).click().perform()
            self.log.info(topLink,"Sub-menu Clicked")
        except:
            self.log.info("Mouse Hover failed on element")
    def clickListView(self):
        self.elementClick(locator=self._listview)

    def clickSortBy(self):
        dropdownClick = Select(self.getElement(locator=self._sortby))
        dropdownClick.select_by_index('5')
        # self.elementClick(locator=self._addtocart,locatorType="xpath")

    def clickAddToCart(self):
        self.elementClick(locator=self._addtocart,locatorType='xpath')

    def verifydesktopadddedsuccessfully(self):
        msgelem = self.waitForElement(locator=self._addedtocardsuccessmsg,locatorType='xpath')
        result = self.isElementDisplayed(element=msgelem)
        return result
    def gotohomepage(self):
        self.elementClick(locator=self._home,locatorType='xpath')

    def clickShoppingCart(self):
        self.elementClick(locator=self._cart,locatorType='xpath')
        self.elementClick(locator=self._viewCart,locatorType='xpath')

    def shippingTax(self):
        self.elementClick(locator=self._estimateShippingandTaxes,locatorType='xpath')
        countryelem = Select(self.getElement(locator=self._TaxCountry))
        countryelem.select_by_value('99')
        stateelem = Select(self.getElement(locator=self._TaxState))
        stateelem.select_by_value('1503')
        self.sendKeys('451452',locator=self._Taxpostalcode)
        self.elementClick(locator=self._getQuotes)
        self.elementClick(locator=self._shippingmethod,locatorType='xpath')
        self.elementClick(locator=self._applyshipping)
        time.sleep(2)
        self.webScroll(direction='down')
        self.elementClick(locator=self._checkOut,locatorType='xpath')

    def enterBillingDetails(self,FirstName,LastName,Address1,City,Postalcode):
        self.elementClick(locator=self._addnewaddress,locatorType='xpath')
        self.sendKeys(FirstName,locator=self._Billingfirstname)
        self.sendKeys(LastName,locator=self._Billinglastname)
        self.sendKeys(Address1,locator=self._BillingAddress1)
        self.sendKeys(City,locator=self._BillingcCity)
        self.sendKeys(Postalcode,locator=self._BillingPostaCode)
        countryelem = self.getElement(locator=self._BillingCountry)
        selectcountry = Select(countryelem)
        selectcountry.select_by_value('223')
        stateelem = self.getElement(locator=self._BillingState)
        selectstate = Select(stateelem)
        selectstate.select_by_value('3635')
        self.elementClick(locator=self._paymentaddressbutton,locatorType='xpath')
        self.elementClick(locator=self._Billingcontinue)

    def selectDeliverydetails(self):
        self.elementClick(locator=self._continueShippingAddress)

    def selectDelieryMethod(self):
        self.elementClick(locator=self._comment,locatorType='name')
        self.elementClick(locator=self._deliverymethodContinue)

    def selectPayementMethod(self):
        self.elementClick(locator=self._agreecheckbox,locatorType='name')
        self.elementClick(locator=self._PaymentMethodContinue)

    def clickConfirmOrder(self):
        self.elementClick(locator=self._confirmorderButton)

    def orderDesktop(self):
        self.clickShowAllDesktop()
        self.clickListView()
        self.clickSortBy()
        self.clickAddToCart()

    def opencart(self,FirstName,LastName,Address1,City,Postalcode):
        self.gotohomepage()
        self.clickShoppingCart()
        self.shippingTax()
        self.enterBillingDetails(FirstName,LastName,Address1,City,Postalcode)
        self.selectDeliverydetails()
        self.selectDelieryMethod()
        self.selectPayementMethod()
        self.clickConfirmOrder()
        time.sleep(2)

    def verifyorderSuccessfull(self):
        result = self.verifyPageTitle(titleToVerify="Your order has been placed!")
        return result


