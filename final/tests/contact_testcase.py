import os, sys, unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from pages import contact_page
from selenium import webdriver
from PIL import Image
from Screenshot import Screenshot_Clipping

class TestContactPage(unittest.TestCase):

    def setUp(self):
        self.ob=Screenshot_Clipping.Screenshot()
        self.SCREENSHOT_FOLDER = r'./screenshots/'
        options = webdriver.ChromeOptions()
        # options.add_argument("start-maximized")
        # to supress the error messages/logs
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(
            options=options, executable_path="final/drivers/chromedriver.exe")
        self.driver.get("https://www.colibri-software.com/contact/")
        # Load the main page. In this case the home page of colibri-software.com.
        self.CONTACT_PAGE = contact_page.ContactPage(self.driver)


    def testcase_TC01(self):
        """
        TC01: Tests the word "Contact" is in title
        """

        # Checks if the word "Contact" is in title
        PAGE_TITLE = self.CONTACT_PAGE.get_title()
        self.assertEqual("Contact", PAGE_TITLE, 'The "Contact" page title is not match')
        
        # Take a screenshot
        self.ob.full_Screenshot(
            self.driver,
            save_path = self.SCREENSHOT_FOLDER,
            image_name='testcase_TC01.png'
        )


    def testcase_TC02(self):
        """
        TC02: Tests "Contact me" form with populates the fields, submits the forms and verifies the success message.
        """

        # enter valid data for the form fields
        self.CONTACT_PAGE.fill_form_by_valid_data()

        # Submitting the form
        self.CONTACT_PAGE.click_submit_form_button()

        # Verifies that success message is displayed
        self.CONTACT_PAGE.success_message_is_displayed(self)

        # Take a screenshot
        self.ob.full_Screenshot(
            self.driver,
            save_path = self.SCREENSHOT_FOLDER,
            image_name='testcase_TC03.png'
        )


    def testcase_TC03(self):
        """
        TC03: Tests "Contact me" form without name field, submit the form and verify the success message is not displayed.
        """
        # enter valid data for the form fields
        self.CONTACT_PAGE.fill_form_by_valid_data()

        # Specified the email field
        self.CONTACT_PAGE.name_input = ''

        # Submitting the form
        self.CONTACT_PAGE.click_submit_form_button()

        # Verifies that success message is not displayed
        self.CONTACT_PAGE.success_message_is_not_displayed(self)

        # Take a screenshot
        self.ob.full_Screenshot(
            self.driver,
            save_path = self.SCREENSHOT_FOLDER,
            image_name='testcase_TC03.png'
        )



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
