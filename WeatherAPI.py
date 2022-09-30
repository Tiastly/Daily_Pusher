# weather module

import requests
import json
import datetime

Icon_Mapping ={
    'clear-day': '晴☀',
    # 'clear-night': 'wi-night-clear',
    'partly-cloudy-day': '局部多云🌤',
    # 'partly-cloudy-night': 'wi-night-cloudy',
    'cloudy': '多云🌥',
    'fog': '雾🌫',
    'wind': '大风🌬',
    'rain': '下雨🌧',
    'sleet': '雨夹雪',
    'snow': '下雪🌨',
    'hail': '下冰雹',
    'thunderstorm': '雷暴🌩',
    }
    
# city location
city = {# "city":[lat,lon]
    "braunschweig":[52.28, 10.45],
    "wolfenbuettel":[52.17, 10.52],
    }

class WeatherReport():
    def __init__(self,today,city=city["braunschweig"]):
        # get the weather information from bright sky API
        self.today = today
        self.location = city
        url = f"https://api.brightsky.dev/weather?lat={self.location[0]}&lon={self.location[1]}&date={today}"
        try:
            print("Sendding request: " + url)
            self.raw_record = requests.get(url).json()
        except requests.HTTPError as e:
            print("fail: " + url)
            print(e, e.response.status_code)
            raise e

    def _weather_record(self)->list:
        #the first processing of raw data
        # return: dict of today's temperature.
        record = []
        for item in self.raw_record["weather"]:
            record.append(item["temperature"])

        return record

    def get_highest(self) -> int:
        #today's hightest temperature.
        record = self._weather_record()
        return max(record)

    def get_lowest(self) -> list:
        #today's lowest temperature.
        record = self._weather_record()
        return min(record)

    def get_weather_icon(self) -> str:
        #today's weather icon
        raw_record = self.raw_record
        icon =  {}
        for item in raw_record["weather"]:
            if 'night' not in item["icon"]:
                icon[item["icon"]] = icon.get(item["icon"],0)+1
                
        res = sorted(icon.items(),key = lambda x:x[1],reverse = True)

        subscribe = Icon_Mapping[res[0][0]]+" "
        if len(res) > 1:
            subscribe += " 转 {}".format(Icon_Mapping[res[1][0]])
        
        return subscribe



if __name__ == "__main__":
    today = datetime.date.today()
    wr = WeatherReport(today, city["braunschweig"])
    print(wr.get_highest())
    print(wr.get_lowest())
    print(wr.get_weather_icon())