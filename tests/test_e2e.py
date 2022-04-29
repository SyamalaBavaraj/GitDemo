import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

# @pytest.mark.usefixtures("setup")--defined in BaseClass File which has knowledge abt fixtures
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitles()

        for card in cards:  # print(card.find_element(By.XPATH, "div/h4/a").text) print the products in Console
            cardText = card.find_element(By.XPATH, "div/h4/a").text
            log.info(cardText)
            if cardText == "Blackberry":
                # Add item to the cart
                card.find_element(By.XPATH, "div/button").click()

        checkOutPage.checkout().click()
        confirmPage = checkOutPage.checkout2()
        self.driver.implicitly_wait(20)
        log.info("Entering the Country name as ind")

        self.driver.find_element(By.ID, "country").send_keys("ind")
        listElements = self.driver.find_elements(By.XPATH, "//div[@class='suggestions']/ul")

        print("Total Suggestions are ", len(listElements))
        for ele in listElements:  # After for loop use print(ele.text), to print Countries with ind
            if ele.text == "India":
                ele.click()
                break

        confirmpage = ConfirmPage(self.driver)
        confirmpage.CheckBox().click()
        confirmpage.checkpurchase().click()
        messagesuccess = confirmpage.getmessage().text
        log.info("Text received from application is " + messagesuccess)
        assert ("Success! Thank you!" in messagesuccess)