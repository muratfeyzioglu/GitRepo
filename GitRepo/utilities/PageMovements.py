from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



class PageMovements:

    def __init__(self, driver):
        self.driver = driver

    def goPageTop(self):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.LEFT_CONTROL + Keys.HOME)

    def goPageBottom(self):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.LEFT_CONTROL + Keys.END)

    def scrollDown(self):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
