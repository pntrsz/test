import os
from behave import fixture, use_fixture, register_type
from playwright.sync_api import sync_playwright
import parse


ENV_URL = os.environ.get('BASE_URL')


@fixture
def init_browser(context):
    with sync_playwright() as pw:
        try:
            provider = context.config.userdata['browser']
        except:
            web_browser = pw.chromium
        else:
            if provider == "safari":
                web_browser = pw.webkit
            elif provider == "firefox":
                web_browser = pw.firefox 
            else:
                web_browser = pw.chromium

        browser = web_browser.launch()
        context.page = browser.new_page(base_url=ENV_URL)
        yield context.page


def before_scenario(context, Scenario):
    use_fixture(init_browser, context)


@parse.with_pattern(r"\d+")
def parse_number(text):
    return int(text)


register_type(Number=parse_number)    