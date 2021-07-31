import json
import statistics
import requests
from jsonDict.jsonDictionary import input_json


class ApiTemp:
    temperatures = []

    def __init__(self):
        self.API_KEY = "166283422f3a88814385f411c263a434"

    def getJsonCitiesTemp(self):
        # converting json string to python dictionary
        json_dict = json.loads(input_json)

        # for every city mentioned in the json, getting the temperature via API and returning
        # to later calculate the variance between API temperature and UI temperature
        for city in json_dict.get("Cities"):
            getcityweather = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={self.API_KEY}")
            if getcityweather.status_code == 200:
                cityDict = json.loads(getcityweather.text)
                cityTemp = cityDict.get("main")['temp']
                print(f"Temp for {city}", cityTemp)
                ApiTemp.temperatures.append(float(cityTemp))
                # print(statistics.variance([float(uiWeather), float(cityTemp)]))
            else:
                print(f"for {city}, error code:", getcityweather.status_code)
        return ApiTemp.temperatures
