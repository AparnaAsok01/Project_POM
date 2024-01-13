

class BasePage:
    def __init__(self, driver):
        self.driver = driver

        # In base page i am just setting up the driver in constructor. so it get invoke automatically at first.
