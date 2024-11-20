import base64
from playwright.sync_api import Page


class BasePage():
    def __init__(self, page: Page, url = None, map_element = None):
        self.page = page
        self.url = url is not None and url or None

        self.map_element = map_element is not None and page.locator(map_element) or None
        self.gdpr = page.get_by_role("button", name="ELFOGADOM")


    def visit(self):            
        self.page.goto(self.url)
        if self.gdpr.count() > 0:
            self.gdpr.click()


    def get_encoded_screenshot(self):
        screenshot = self.map_element.screenshot(type="jpeg", quality=40, animations="disabled", scale="css")
        return base64.b64encode(screenshot)
    

    def get_map_element(self):
        return self.map_element