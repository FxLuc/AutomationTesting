from multiprocessing.pool import INIT
import os, sys, unittest

from pytz import country_timezones
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from pages import contact_page
from selenium import webdriver
from PIL import Image
from Screenshot import Screenshot_Clipping

class CounterIncrement:

    counter = 0

    def __init__(self):
        CounterIncrement.counter += 1 


class TestContactPage(unittest.TestCase):


    def setUp(self):
        self.counter = CounterIncrement()
        self.ob=Screenshot_Clipping.Screenshot()
        self.SCREENSHOT_FOLDER = r'./final/screenshots/contact/'
        options = webdriver.ChromeOptions()

        
        # options.add_argument("start-maximized")
        # to supress the error messages/logs
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(
            options=options, executable_path="final/drivers/chromedriver.exe")
        self.driver.get("https://www.colibri-software.com/contact/")
        # Load the main page. In this case the home page of colibri-software.com.
        self.CONTACT_PAGE = contact_page.ContactPage(self.driver)


    # def testcase_TC01(self):
    #     """
    #     TC01: Tests the word "Contact" is in title
    #     """

    #     # Checks if the word "Contact – Colibri Software" is in title
    #     PAGE_TITLE = self.driver.title
    #     self.assertEqual("Contact – Colibri Software", PAGE_TITLE, 'The "Contact" page title is not match')


    # def testcase_TC02(self):
    #     """
    #     TC02: Tests "Contact me" form with populates the fields, submits the forms and verifies the success message.
    #     """

    #     # enter valid data for the form fields
    #     self.CONTACT_PAGE.fill_form_by_valid_data()

    #     # Submitting the form
    #     self.CONTACT_PAGE.click_submit_form_button()

    #     # Verifies that success message is displayed
    #     self.CONTACT_PAGE.success_message_is_displayed(self)

    def testcase_TC03(self):
        """
        TC03: Tests "Contact me" form without name field, submit the form and verify the success message is NOT displayed.
        """
        # enter valid data for the form fields
        self.CONTACT_PAGE.fill_form_by_valid_data()

        # Specified the email field
        self.CONTACT_PAGE.name_input = ''

        # Submitting the form
        self.CONTACT_PAGE.click_submit_form_button()

        # Verifies that success message is not displayed
        self.CONTACT_PAGE.success_message_is_not_displayed(self)


    def testcase_TC04(self):
        """
        TC04: Tests "Contact me" form with blank name field, submit the form and verify the success message is NOT displayed.
        """

        # enter valid data for the form fields
        self.CONTACT_PAGE.fill_form_by_valid_data()

        # Specified the email field
        self.CONTACT_PAGE.name_input = ' '

        # Submitting the form
        self.CONTACT_PAGE.click_submit_form_button()

        # Verifies that success message is not displayed
        self.CONTACT_PAGE.success_message_is_not_displayed(self)


    # def testcase_TC05(self):
    #     """
    #     TC05: Tests "Contact me" form without name field, submit the form and verify that ERROR message is displayed.
    #     """

    #     # enter valid data for the form fields
    #     self.CONTACT_PAGE.fill_form_by_valid_data()

    #     # Specified the email field
    #     self.CONTACT_PAGE.name_input = ''

    #     # Submitting the form
    #     self.CONTACT_PAGE.click_submit_form_button()

    #     # Verifies that name field error message is displayed
    #     self.CONTACT_PAGE.name_field_error_is_displayed(self)


    # def testcase_TC06(self):
    #     """
    #     TC06: Tests "Contact me" form with blank name field, submit the form and verify that ERROR message is displayed.
    #     """

    #     # enter valid data for the form fields
    #     self.CONTACT_PAGE.fill_form_by_valid_data()

    #     # Specified the email field
    #     self.CONTACT_PAGE.email_input = ' '

    #     # Submitting the form
    #     self.CONTACT_PAGE.click_submit_form_button()

    #     # Verifies that email field error message is displayed
    #     self.CONTACT_PAGE.email_field_error_is_displayed(self)


    # def testcase_TC07(self):
    #     """
    #     TC07: Tests "Contact me" form with invalid email field, submit the form and verify that email flied ERROR message is displayed.
    #     """

    #     # enter valid data for the form fields
    #     self.CONTACT_PAGE.fill_form_by_valid_data()

    #     # Specified the email field
    #     self.CONTACT_PAGE.email_input = "john@whocom"

    #     # Submitting the form
    #     self.CONTACT_PAGE.click_submit_form_button()

    #     # Verifies that email field invalid message is displayed
    #     self.CONTACT_PAGE.email_field_invalid_is_displayed(self)


    # def testcase_TC08(self):
    #     """
    #     TC08: Tests "Contact me" form with invalid email field, submit the form and verify the success message is not displayed.
    #     """

    #     # enter valid data for the form fields
    #     self.CONTACT_PAGE.fill_form_by_valid_data()

    #     # Specified the email field
    #     self.CONTACT_PAGE.email_input = "john@whocom"

    #     # Submitting the form
    #     self.CONTACT_PAGE.click_submit_form_button()

    #     # Verifies that success message is not displayed
    #     self.CONTACT_PAGE.success_message_is_not_displayed(self)


    def tearDown(self):
        # Take a screenshot
        # self.ob.full_Screenshot(
        #     self.driver,
        #     save_path = self.SCREENSHOT_FOLDER,
        #     image_name='testcase_TC'+ str(self.counter.counter) + '.png'
        # )
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()