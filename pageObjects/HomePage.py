from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//ul[@class='navbar-nav']/li[2]")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, 'email')
    password = (By.ID, 'exampleInputPassword1')
    checkbox = (By.ID, 'exampleCheck1')
    gender = (By.ID, 'exampleFormControlSelect1')
    submit = (By.XPATH, "//input[@type='submit']")
    successmsg = (By.CLASS_NAME, 'alert-success')

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
        # driver.find_element(By.XPATH, "//ul[@class='navbar-nav']/li[2]")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getsuccessmessage(self):
        return self.driver.find_element(*HomePage.successmsg)