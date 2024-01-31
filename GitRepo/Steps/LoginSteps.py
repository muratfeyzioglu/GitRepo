from pageObjects.PageModel import PageModel
from utilities.PageMovements import PageMovements
from utilities.readProperties import ReadConfig
from utilities.XpathCreaterForItem import XpathCreaterForItem

class LoginSteps:



    def __init__(self, driver):
        self.driver = driver

    def LoginSteps(self):
        loginPageModel = PageModel(self.driver)

        username = "murat.feyzioglu@xinerji.com"
        password = "Murat12*"


        loginPageModel.clickLoginButton()
        loginPageModel.setUsername(username)
        loginPageModel.setPassword(password)

        loginPageModel.clickSing()
















