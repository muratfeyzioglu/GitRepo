import sys

import pytest

sys.path.append('/usr/src/app')
import time
import traceback
import pandas as pd
from selenium import webdriver

from Cases.LoginSteps import LoginSteps

from utilities.customLogger import LogGen
from pageObjects.PageModel import PageModel
from Controller.GetDataFromExcel import GetDataFromExcel
from utilities.DayCounter import DayCounter
from selenium.webdriver.common.by import By

@pytest.fixture
def setup_database():
    print("Setup database")
    yield
    print("Teardown database")


class Test:
    def teardown_method(self, method):
        print("teardown")
    def test_example(self):

        baseUrl = "http://example.url"

        driver = webdriver.Chrome()

        """logger"""
        logger = LogGen.loggenWeld()

        loginSteps = LoginSteps(driver)
        PageModel = PageModel(driver)
        getDataFromExcel = GetDataFromExcel()
        dayCounter = DayCounter()

        driver.maximize_window()
        driver.get(baseUrl)

        loginSteps.LoginSteps()

        """row and column lengths in excel are assigned to a variable"""
        num_rows, num_cols = getDataFromExcel.getData().shape

        """The process is repeated as many times as the row found in excel"""
        for i in range(1, num_rows):
            logger.info(f"Satır No:{i}")
            """takes data from excel and assigns it to variables."""
            getDataFromExcel.fillDatas(i)

            """is assigned to the given variables filled from excel.
                The reason for reassigning to variables is 
                to facilitate their availability in the corresponding automation part."""
            value1 = getDataFromExcel.value1
            value2 = getDataFromExcel.value2


            logger.info(
                f"value1: {value1}, " + f"value2: {value2}"
            )

            time.sleep(5)
            PageModel.clickButton()
            PageModel.clickDropdown()
            PageModel.selectSpanElement(value1)

            PageModel.clickDropdown()
            PageModel.selectSpanElement(value2)

            print(dayCounter.getToday())
            PageModel.setField(dayCounter.getToday())


            if value2 == "X" or value2 == "Y":
                PageModel.setField("text")


            """logis of the "if the excel cell is nan or not" """
            if pd.isna(value1):
                print("value1 nan")
            else:
                valueFromWeb = PageModel.getField()
                try:
                    assert valueFromWeb == value1,  getDataFromExcel.changeColor(i, 20)
                except AssertionError:
                    traceback.print_exc()  # Print the traceback for debugging purposes

        driver.quit()

    def kodSplit(self, text):
        split_text = text.split(" ")
        text = split_text[0].strip()
        return text