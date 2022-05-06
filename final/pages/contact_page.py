from selenium.webdriver.common.by import By
from .base_page import BasePage
from .contact_locators import AdditionalInfoElement, CompanyNameElement, EmailElement, EmailFeedbackElement, NameElement, NameFeedbackElement, SubmitElement, ComfirmationElement
from selenium.common.exceptions import TimeoutException


class ContactPage(BasePage):
    """
    Contact page action methods come here
    """

    CONFIRM_MESSAGE = "Thanks for contacting us! We will be in touch with you shortly."
    SUCCESS_MESSAGE_STILL_DISPLAYED = "The success message still displayed."
    ERROR_MESSAGE_NOT_DISPLAYED = "The error message is not displayed."
    ERROR_MESSAGE_REQUIRED = "This field is required."
    EMAIL_INVALID_ERROR_MESSAGE = "Please enter a valid email address."

    # Declares text input fields
    name_input = NameElement()
    company_name_input = CompanyNameElement()
    email_input = EmailElement()
    additional_info_input = AdditionalInfoElement()

    name_input_feedback = NameFeedbackElement()
    email_input_feedback = EmailFeedbackElement()
    submit_element = SubmitElement()

    comfirmation_element = ComfirmationElement()

    def get_title(self):
        """
        Get the text appears in page title
        """
        return self.driver.title

    def fill_form_by_valid_data(self):
        """
        Enter valid data for the form fields
        """
        self.name_input = 'John Wick'
        self.company_name_input = 'John Wick Company'
        self.email_input ='johnwick@gmail.com'
        self.additional_info_input = "Excuse me! I\'m just made automation testing on your website"

    def click_submit_form_button(self):
        """
        Submits the form
        """
        self.submit_element.click()

    def get_success_message(self):
        element = self.comfirmation_element.find_element(By.TAG_NAME, "p")
        return element.text

    def name_field_error_is_displayed(self, context):
        """
        Verifies that name field error message is displayed
        """
        try:
            ERROR_MESSAGE_REQUIRED = self.name_input_feedback.text
            context.assertEqual(self.ERROR_MESSAGE_REQUIRED, ERROR_MESSAGE_REQUIRED, self.ERROR_MESSAGE_NOT_DISPLAYED)
        except TimeoutException:
            assert False, self.ERROR_MESSAGE_NOT_DISPLAYED

    def email_field_error_is_displayed(self, context):
        """
        Verifies that email field error message is displayed
        """
        try:
            ERROR_MESSAGE_REQUIRED = self.email_input_feedback.text
            context.assertEqual(self.ERROR_MESSAGE_REQUIRED, ERROR_MESSAGE_REQUIRED, self.ERROR_MESSAGE_NOT_DISPLAYED)
        except TimeoutException:
            assert False, self.ERROR_MESSAGE_NOT_DISPLAYED
    
    def email_field_invalid_is_displayed(self, context):
        """
        Verifies that email field invalid message is displayed
        """
        try:
            EMAIL_INVALID_ERROR_MESSAGE = self.email_input_feedback.text
            context.assertEqual(self.EMAIL_INVALID_ERROR_MESSAGE, EMAIL_INVALID_ERROR_MESSAGE, self.ERROR_MESSAGE_NOT_DISPLAYED)
        except TimeoutException:
            assert False, self.ERROR_MESSAGE_NOT_DISPLAYED

    def success_message_is_not_displayed(self, context):
        """
        Verifies that success message is not displayed
        """
        try:
            SUCCESS_MESSAGE = self.get_success_message()
            context.assertNotEqual(self.CONFIRM_MESSAGE, SUCCESS_MESSAGE, self.SUCCESS_MESSAGE_STILL_DISPLAYED)
        except TimeoutException:
            pass

    def success_message_is_displayed(self, context):
        """
        Verifies that success message is displayed
        """
        try:
            SUCCESS_MESSAGE = self.get_success_message()
            context.assertEqual(self.CONFIRM_MESSAGE, SUCCESS_MESSAGE, self.SUCCESS_MESSAGE_STILL_DISPLAYED)
        except TimeoutException:
            assert False, self.SUCCESS_MESSAGE_STILL_DISPLAYED