"""from selenium import webdriver
from selenium.webdriver.support.ui import Select


# class Sampleusage():

    # driver = webdriver.Chrome()

    # Methods
    # select = Select(driver.find_element_by_id('days'))
    # select.select_by_value(14)
    """
import time
import autoit
import re
from pyrobot import RoboBrowser
import runtime
# from pywinauto import application
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.chrome

elem = ActionChains(driver)
elem.key_down(10)
