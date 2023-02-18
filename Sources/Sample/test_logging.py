import logging


class Test:
    def __init__(self) -> None:
        logging.basicConfig(level = logging.DEBUG,format = '[%(asctime)s] %(levelname)s [%(module)s:%(lineno)s] %(message)s')
        self.Logger = logging.getLogger()
        self.Logger.info("Printed info message")
        self.Logger.debug("Printed debug message")
        self.Logger.warning("WARN")


class Test1(Test):
    def __init__(self) -> None:
        super().__init__()
        self.Logger.info("Message from Sub Class")

if __name__ == "__main__":
    t = Test1()