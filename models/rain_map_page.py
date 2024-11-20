from playwright.sync_api import Page
from models.base_page import BasePage


class RainMapPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, "/csapadek", "img[name='csap24a']")