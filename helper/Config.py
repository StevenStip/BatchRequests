__author__ = 'steven'
import configparser


class Config:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    def get_configsection(self, section):
        dict1 = {}
        options = self.config.options(section)
        for option in options:
            dict1[option] = self.config.get(section, option)

        return dict1

    def get_configoption(self, section, option):
        return self.config.get(section, option)



