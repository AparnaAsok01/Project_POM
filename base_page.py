# POM (PAGE OBJECT MODEL) - is a design pattern used in selenium automation testing to enhance test maintenance
# and readability by seperating the page structure and functionalities.

# POM - Can be implemented by other programming languages as well

# Components of POM:
# Pages: Each webpage or section of a webpage is represented by a seperate class.
# These classes contain the page's elements and methods to interact with those elements.

# Page classes: It contains locators and methods that perform actions on those elements.
# They encapsulate the functionalities of the pages.

# Test classes: Test cases / scripts interact with the page classes rather than directly intercacting with
# the web elements. The seperation increases the maintainability of the tests and reduces code duplication.

class BasePage:
    def __init__(self, driver):
        self.driver = driver

        # In base page iam just setting up the driver in constructor. so it get invoke automatically at first.
