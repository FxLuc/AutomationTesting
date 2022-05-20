from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

TIMEOUT_MAX = 10
TIMEOUT_ERROR_MESSAGE = "Timed out waiting for the element to appear."

class BasePageFieldElement(object):
    """
    Base page class that is initialized on every page object class.
    """

    def __set__(self, obj, value):
        """
        Sets the text to the value supplied
        """
        driver = obj.driver
        WebDriverWait(driver, TIMEOUT_MAX).until(lambda driver: driver.find_element(By.ID, self.element_id), TIMEOUT_ERROR_MESSAGE)
        driver.find_element(By.ID, self.element_id).clear()
        driver.find_element(By.ID, self.element_id).send_keys(value)


    def __get__(self, obj, owner):
        """
        Gets the text of the specified object
        """
        driver = obj.driver
        element = WebDriverWait(driver, TIMEOUT_MAX).until(lambda driver: driver.find_element(By.ID, self.element_id), TIMEOUT_ERROR_MESSAGE)
        return element.get_attribute("value")


class BasePageElement(object):
    """
    Base page class that is initialized on every page object class.
    """

    def __get__(self, obj, owner):
        """
        Gets the element of the specified element_id
        """
        driver = obj.driver
        element = WebDriverWait(driver, TIMEOUT_MAX).until(lambda driver: driver.find_element(By.ID, self.element_id), TIMEOUT_ERROR_MESSAGE)
        return element

class BasePageElementByClass(object):
    """
    Base page class that is initialized on every page object class.
    """

    def __get__(self, obj, owner):
        """
        Gets the element of the specified element_id
        """
        driver = obj.driver
        elements = WebDriverWait(driver, TIMEOUT_MAX).until(lambda driver: driver.find_elements(By.CLASS_NAME, self.element_class_name), TIMEOUT_ERROR_MESSAGE)
        return elements


class BasePage(object):
    """
    Base class to initialize the base page that will be called from all pages
    """

    def __init__(self, driver):
        self.driver = driver
