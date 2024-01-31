from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from utilities.XpathCreaterForItem import XpathCreaterForItem
from utilities.CssController import CssContoller

"""This Clas"""
class PageModel:

    cssController = CssContoller()

    button_xpath = "xpath"
    dropdown_id = "id"

    price_input_id = "price_input_id"

    #CSS
    """some spacial element, we may use the css selector.
    That's why created a cssController page for the associate with ID
    """
    price_css = cssController.createCssForInputWeld(price_input_id)


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.xpathCreater = XpathCreaterForItem()

    def clickButton(self):
        element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.price_css)))
        element.click()

    def clickButtonCSS(self):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_xpath)))
        element.click()

    def clickDropdown(self):
        element = self.wait.until(EC.element_to_be_clickable((By.ID, self.dropdown_id)))
        element.click()

    def setField(self, key):
        element = self.wait.until(EC.visibility_of_element_located((By.ID, self.price_input_id)))
        element.send_keys(key)
        element.click()

    def getField(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, self.price_input_id))).text


    def selectSpanElement(self, key):
        """Locate the Span element containing the specified Text parameter.
        Refer to the related Class for further details."""
        xpath = self.xpathCreater.createXpathForSpan(key)
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()


    def selectSpanElementEquals(self, key):
        """Locate the Span element equals the specified Text parameter.
        Refer to the related Class for further details."""
        xpath = self.xpathCreater.createXpathForSpanEqual(key)
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

    def clickPricesButton(self, key):
        """click from a selected fixed element to an element higher in the hierarchy"""
        xpath = "//h5[contains(text(),'" + key + "')]/../../..//button"
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element.click()