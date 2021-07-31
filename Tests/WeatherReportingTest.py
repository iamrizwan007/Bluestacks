from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from jsonDict.jsonDictionary import input_json
from PageObjects.HomepageObj import Homepage
from PageObjects.WeatherDetailspageObj import WeatherDetails
from TemperatureViaAPI.APITemperature import ApiTemp
import json
import statistics


class TestWeatherReporting:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://weather.com/")

    def getWeatherInfoViaUI(self):
        hp = Homepage(self.driver)
        wd = WeatherDetails(self.driver)
        hp.searchCity("Delhi")
        return wd.getCurrentTemp()

    def getWeatherInfoViaAPI(self):
        apiObj = ApiTemp()
        temperatures = apiObj.getJsonCitiesTemp()
        return temperatures

    def calculateVariance(self, samples, UISample):
        jsonDict = json.loads(input_json)
        variance = jsonDict.get("variance")
        for sample in samples:
            data_sample = [UISample, sample]
            print(data_sample)
            if statistics.variance(data_sample) <= variance:
                print(f"calculated variance is {statistics.variance(data_sample)} : pass")
            else:
                print(f"calculated variance is {statistics.variance(data_sample)} :exceed variance range")


test = TestWeatherReporting()
temperatureFromUI = test.getWeatherInfoViaUI()
temperatureFromAPI = test.getWeatherInfoViaAPI()
print("Temperature from UI:",temperatureFromUI)
print("Temperature from API for the cities in json", temperatureFromAPI)
test.calculateVariance(temperatureFromAPI, temperatureFromUI)