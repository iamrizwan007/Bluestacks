from selenium import webdriver
from selenium.webdriver.common.by import By


class WeatherDetails:
    currentTemp = (By.XPATH, "//div[@class='CurrentConditions--primary--39Y3f']/span")
    symbol = "°"

    def __init__(self, driver):
        self.driver = driver

    def getCurrentTemp(self):
        temperture = self.driver.find_element(*WeatherDetails.currentTemp).text
        print("Current Temperature:", temperture)
        return float(temperture.replace(WeatherDetails.symbol, ""))