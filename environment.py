import os, parse
from dotenv import load_dotenv
from datetime import datetime, timezone
from behave import fixture, use_fixture, register_type
from playwright.sync_api import sync_playwright


ENV_URL = os.environ.get('BASE_URL')


@fixture
def create_dir(name):
    if not os.path.isdir(name):
        os.mkdir(name)

@fixture
def prepare_dir(context):
    out_dir = "./out/"
    use_fixture(create_dir, out_dir)
    with open(out_dir + ".gitignore", "w") as file:
                file.write("*")
    stamp_dir = "./out/"+ datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S") + "/"
    context.out = stamp_dir
    use_fixture(create_dir, stamp_dir)


@fixture
def print_env(context):
    load_dotenv()
    env_name = os.getenv('ENV_NAME', "PROD")
    print(f'Test executed on {env_name} environment!')


def before_all(context):
    use_fixture(prepare_dir, context)
    use_fixture(print_env, context)

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