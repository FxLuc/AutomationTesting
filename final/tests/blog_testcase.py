from multiprocessing.pool import INIT
import os, sys, unittest

from pytz import country_timezones
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from pages import blog_page
from selenium import webdriver
from PIL import Image
from Screenshot import Screenshot_Clipping

class CounterIncrement:

    counter = 0

    def __init__(self):
        CounterIncrement.counter += 1 


class TestBlogPage(unittest.TestCase):


    def setUp(self):
        self.counter = CounterIncrement()
        self.ob=Screenshot_Clipping.Screenshot()
        self.SCREENSHOT_FOLDER = r'./final/screenshots/blog/'
        options = webdriver.ChromeOptions()
        # options.add_argument("start-maximized")
        # to supress the error messages/logs
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options, executable_path="final/drivers/chromedriver.exe")
        self.driver.get("https://www.colibri-software.com/insights/")
        # Load the main page. In this case the home page of colibri-software.com.
        self.BLOG_PAGE = blog_page.BlogPage(self.driver)


    def testcase_TC01(self):
        """
        TC01: Tests the word "Insights" is in title
        """
        # Checks if the word "Insights – Colibri Software" is in title
        PAGE_TITLE = self.driver.title
        self.assertEqual("Insights – Colibri Software", PAGE_TITLE, 'The "Insights" page title is not match')

    def testcase_TC02(self):
        """
        TC02: Tests the post card element must be match
        """
        index = 0
        for index in range(len(self.BLOG_PAGE.post_card_elements)):
            next_page_title = self.BLOG_PAGE.post_card_elements[index].text + " – Colibri Software"
            self.BLOG_PAGE.post_card_elements[index].click()
            PAGE_TITLE = self.driver.title
            self.assertEqual(next_page_title, PAGE_TITLE, 'Page title is not match')
            self.driver.back()

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