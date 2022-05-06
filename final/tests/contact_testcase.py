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


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
