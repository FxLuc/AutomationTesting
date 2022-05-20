from .base_page import BasePageElement, BasePageFieldElement


class NameElement(BasePageFieldElement):
    """
    This class gets the search element by the xPATH
    """
    locator = "//input[@id='wpforms-236-field_0']"


class NameFeedbackElement(BasePageElement):
    locator = "//label[@id='wpforms-236-field_0-error']"



class CompanyNameElement(BasePageFieldElement):
    locator = "//input[@id='wpforms-236-field_4']"


class EmailElement(BasePageFieldElement):
    locator = "//input[@id='wpforms-236-field_1']"


class EmailFeedbackElement(BasePageElement):
    locator = "//label[@id='wpforms-236-field_1-error']"


class AdditionalInfoElement(BasePageFieldElement):
    locator = "//textarea[@id='wpforms-236-field_2']"


class SubmitElement(BasePageElement):
    locator = "//button[@id='wpforms-submit-236']"


class ComfirmationElement(BasePageElement):
    locator = "//div[@id='wpforms-confirmation-236']"
