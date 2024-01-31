from datetime import date
from datetime import timedelta

class DayCounter:
    today = date.today()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)


    def getToday(self):
        today = self.today.strftime("%d.%m.%Y")
        return today

    def getToday1(self):
        today = self.today
        return today

    def getYesterday(self):
        yesterday = self.yesterday.strftime("%d.%m.%Y")
        return yesterday

    def getTomorrow(self):
        tomorrow = self.tomorrow.strftime("%d.%m.%Y")
        return tomorrow


