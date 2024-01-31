
class XpathCreaterForItem:

    def createXpathForSpan(self, item):
        xpath = "//span[contains(text(),'" + item + "')]"
        return xpath

    def createXpathForSpanEqual(self, item):
        xpath = "//span[text()='" + item + "']"
        return xpath