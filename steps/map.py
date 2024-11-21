from behave import *
from models.heat_map_page import HeatMapPage
from models.rain_map_page import RainMapPage
from playwright.sync_api import expect


@when(u'I visit the rain map')
def visit_rain_map_site(context):
    rain_map_page = RainMapPage(context.page)
    rain_map_page.visit()
    context.page = rain_map_page


@when(u'I visit the heatmap')
def visit_heat_map_site(context):
    heat_map_page = HeatMapPage(context.page)
    heat_map_page.visit()
    context.page = heat_map_page


@then(u'last 24 hours rain activity map is included')
@then(u'actual heat map is included')
def map_is_included(context):
    heat_map_page = context.page
    context.log = heat_map_page.get_encoded_screenshot()
    expect(heat_map_page.map_element).to_have_count(1)