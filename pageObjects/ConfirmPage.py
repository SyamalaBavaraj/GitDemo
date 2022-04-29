from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchasebnt = (By.CSS_SELECTOR, "[type='submit']")
    successmessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def CheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)
    # driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")

    def checkpurchase(self):
        return self.driver.find_element(*ConfirmPage.purchasebnt)
    # driver.find_element(By.CSS_SELECTOR, "[type='submit']")

    def getmessage(self):
        return self.driver.find_element(*ConfirmPage.successmessage)