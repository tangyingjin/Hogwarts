from selenium.webdriver.common.by import By


class RegisterPage():
    def __init__(self, driver):
        self.driver = driver

    def registerpage(self, corpname):
        self.driver.find_element(By.ID, 'corp_name').send_keys(corpname)
        self.driver.find_element(By.ID, 'submit_btn').click()
