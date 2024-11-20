from behave import *
from playwright.sync_api import expect
from helpers.file_writer import save_to_file
from models.weather_page import WeatherPage


@given(u'the main page displayed')
def load_main_page(context):
    weather_page = WeatherPage(context.page)
    weather_page.visit()


@then(u'dress advisement is written')
def dress_advisement_is_written(context):
    weather_page = WeatherPage(context.page)
    context.log=weather_page.dress_advise_text.inner_text()
    expect(weather_page.dress_advise_text).not_to_be_empty()
    expect(weather_page.dress_advise_text).to_be_visible()


@then(u'rain forecast is shown at laast for "{day_interval:Number}" days')
def rain_forecast_is_shown(context, day_interval):
    weather_page = WeatherPage(context.page)
    weather_page.count_rain_forecast(day_interval)
    context.log=weather_page.daily_rain_forecast
    assert len(weather_page.daily_rain_forecast) == day_interval
    

@then(u'can save the result as "{extension}"')
def save_result(context, extension):
    save_to_file(extension, context.scenario.name, context.log)