import configparser

class ReadConfig:


    @staticmethod
    def getAppUrl():
        config = configparser.RawConfigParser()
        config.read(".\\Configurations\\config.ini")
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUsername():
        config = configparser.RawConfigParser()
        config.read(".\\Configurations\\config.ini")
        username = config.get("common info", "username")
        return username

    @staticmethod
    def getPassword():
        config = configparser.RawConfigParser()
        config.read(".\\Configurations\\config.ini")
        password = config.get("common info", "password")
        return password

    @staticmethod
    def getUserMail():
        config = configparser.RawConfigParser()
        config.read("C:\\Configurations\\config.ini")
        userMail = config.get("common info", "userMail")
        return userMail

