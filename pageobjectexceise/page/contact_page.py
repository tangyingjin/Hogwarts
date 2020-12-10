import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from pageobjectexceise.page.base_page import BasePage


class Contact(BasePage):


    def add_member(self):
        self._driver.find_element(By.ID,'username').send_keys('tangyingying')
        self._driver.find_element(By.ID,'memberAdd_acctid').send_keys('123')
        self._driver.find_element(By.CSS_SELECTOR,'.ww_radio[value="2"]').click()
        self._driver.find_element(By.CSS_SELECTOR,'.ww_dropdownMenu li[data-value="886"]').click()
        self._driver.find_element(By.ID,'memberAdd_phone').send_keys('12345678901')
        self._driver.find_elements(By.CSS_SELECTOR,'.js_btn_save')[2].click()

