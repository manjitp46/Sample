import logging

# import logging


class BaseObject():
    def __init__(self) -> None:
        logging.basicConfig(level = logging.DEBUG,format = '[%(asctime)s] %(levelname)s [%(module)s:%(lineno)s] %(message)s')
        logging.StreamHandler()
        self.Logger = logging.getLogger()
        self.Logger.info("Printed info message")
        self.Logger.debug("Printed debug message")
        self.Logger.warning("WARN")