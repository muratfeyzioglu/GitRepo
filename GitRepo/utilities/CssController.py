class CssContoller:

    def createCssForMatInput(self, componentID):
        cssXpath = "mat-input#" + componentID + " :nth-child(1) > div > div > div > input"
        return cssXpath

    def createCssForMatMultiAutoComplete(self, componentID):
        cssXpath = "x-mat-multi-autocomplete#" + componentID + ":nth-child(1) > div > div > x-mat-autocomplete > div > mat-form-field > div > div > div > input"
        return cssXpath

    def createCssForMatAutoComplete(self, componentID):
        cssXpath = "x-mat-autocomplete#" + componentID + ":nth-child(1) >  div > mat-form-field > div > div > div > input"
        return cssXpath

    def createCssForMatDatePicker(self, componentID):
        cssXpath = "x-mat-datepicker#" + componentID + " :nth-child(2) > div > div > div >input"
        return cssXpath

    def createCssForXDatePicker(self, componentID):
        cssXpath = "x-datepicker#" + componentID + ":nth-child(2) > div > input"
        return cssXpath

    def createCssForMatSelectList(self, componentID):
        cssXpath = "mat-selectlist#" + componentID + ":nth-child(1) > mat-form-field > div > div > div > mat-select"
        return cssXpath

    def createCssForLabel(self, componentID):
        cssXpath = "x-mat-autocomplete#" + componentID + ":nth-child(1) > div > mat-form-field > div > div > div > span > label > mat-label"
        return cssXpath

    def createCssForXAutoComplete(self, componentID):
        cssXpath = "x-autocomplete#" + componentID + ":nth-child(2) > div > p-autocomplete > span > input"
        return cssXpath

    def createCssForInputWeld(self, componentID):
        cssXpath = "#" + componentID + " > span > input"
        return cssXpath

    def createCssForAutoCompleteWeld(self, componentID):
        cssXpath = "#" + componentID + " > p-autocomplete > span > input"
        return cssXpath