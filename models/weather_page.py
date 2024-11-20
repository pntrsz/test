from playwright.sync_api import Page
from models.base_page import BasePage
import re


class WeatherPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, "/idojaras/Budapest")
        self.daily_rain_forecast = []
        
        self.dress_advise_text = page.locator(".what-to-wear")
        self.forecast_days = page.locator(".dailyForecastCol")
        self.day_info = page.locator(".dfIconAlert").locator('a')
        self.daily_rain = page.locator(".rainlevel-container")


    def count_rain_forecast(self, amount):
        pattern = re.compile(r'<.*?>')
        for i in range(amount):
            line = []
            forecast_date = re.sub(pattern, ' ', self.day_info.nth(i + 1).get_attribute("data-bs-original-title"))
            is_rain_foreseen = self.forecast_days.nth(i + 1).filter(has=self.daily_rain).count() == 1
            line.append(forecast_date)
            line.append("Yes" if is_rain_foreseen else "No")
            self.daily_rain_forecast.append(line)
