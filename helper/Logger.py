import helper.Config

__author__ = 'steven'
import logging


class Logger:

    def __init__(self):
        self.config = helper.Config.Config()
        conf = self.config
        logging.basicConfig(filename=conf.get_configoption("Logging", "path"),
                            level=conf.get_configoption("Logging", "level"),
                            format= "%(asctime)s\t%(levelname)s\t%(message)s")

    def debug(self, message):
        #print(datetime.datetime())
        logging.debug(message)

    def info(self, message):
        logging.info(message)

    def warning(self, message):
        logging.warning(message)

def main():
    log = Logger()
    log.debug("debug")
    log.warning("warn")
    log.info("info")


if __name__ == '__main__':
    main()
