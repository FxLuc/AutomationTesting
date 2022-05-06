from .base_page import BasePageElement, BasePageFieldElement


class NameElement(BasePageFieldElement):
    """
    This class gets the search text from the specified ID
    """
    # The ID for text box where name is entered
    locator = "wpforms-236-field_0"


class NameFeedbackElement(BasePageElement):
    locator = "wpforms-236-field_0-error"


class CompanyNameElement(BasePageFieldElement):
    locator = "wpforms-236-field_4"


class EmailElement(BasePageFieldElement):
    locator = "wpforms-236-field_1"


class EmailFeedbackElement(BasePageElement):
    locator = "wpforms-236-field_1-error"


class AdditionalInfoElement(BasePageFieldElement):
    locator = "wpforms-236-field_2"


class SubmitElement(BasePageElement):
    locator = "wpforms-submit-236"


class ComfirmationElement(BasePageElement):
    locator = "wpforms-confirmation-236"
