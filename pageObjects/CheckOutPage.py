from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    checkbutton = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    checkbutton2 = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)
    # driver.find_elements(By.XPATH, "//div[@class='card h-100']") for this object

    def checkout(self):
        return self.driver.find_element(*CheckOutPage.checkbutton)
    # driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()

    def checkout2(self):
        self.driver.find_element(*CheckOutPage.checkbutton2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

    # driver.find_element(By.XPATH, "//button[@class='btn btn-success']")