from selenium.webdriver.common.by import By

class SelectFromTreeNode:

    def selectItemFromTreeNodeList(self, cardNo, items ):

        for i in items:
            if cardNo in i.text:
                print(i.text)
                i.click()