from .base_page import BasePageElementBySelector


class PostCardElement(BasePageElementBySelector):
    """
    This class gets the search element by the xPATH
    """
    locator = "a[class='eael-grid-post-link']"