import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getdata):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        log.info("firstname is" + getdata['firstname'])
        homePage.getName().send_keys(getdata['firstname'])
        homePage.getemail().send_keys(getdata['email'])
        homePage.getpassword().send_keys(getdata['password'])
        homePage.getcheckbox().click()

        # select class provide the methods to handle the options in dropdown
        self.selectOptionByText(homePage.getgender(), getdata['gender'])
        homePage.getsubmit().click()

        message = homePage.getsuccessmessage().text

        assert 'success' in message
        # print(message)
        self.driver.refresh()   # It will Refresh the URL for the Second set of Data

    @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
    def getdata(self, request):
        return request.param