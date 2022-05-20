from .base_page import BasePageElement, BasePageFieldElement


class NameElement(BasePageFieldElement):
    """
    This class gets the search text from the specified ID
    """
    # The ID for text box where name is entered
    element_id = "wpforms-236-field_0"


class NameFeedbackElement(BasePageElement):
    element_id = "wpforms-236-field_0-error"


class CompanyNameElement(BasePageFieldElement):
    element_id = "wpforms-236-field_4"


class EmailElement(BasePageFieldElement):
    element_id = "wpforms-236-field_1"


class EmailFeedbackElement(BasePageElement):
    element_id = "wpforms-236-field_1-error"


class AdditionalInfoElement(BasePageFieldElement):
    element_id = "wpforms-236-field_2"


class SubmitElement(BasePageElement):
    element_id = "wpforms-submit-236"


class ComfirmationElement(BasePageElement):
    element_id = "wpforms-confirmation-236"
