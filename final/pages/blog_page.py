from selenium.webdriver.common.by import By
from .base_page import BasePage
from .blog_locators import PostCardElement
from selenium.common.exceptions import TimeoutException


class BlogPage(BasePage):
    """
    Blog page action methods come here
    """

    post_card_elements = PostCardElement()


    def click_post_title_link(self):
        """
        Click the title to follow ling
        """
        self.post_card_elements.click()
