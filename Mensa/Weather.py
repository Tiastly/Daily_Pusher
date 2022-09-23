# 天气组件
key = "5f088a530f1b417dbdd182603222309"
def get_weather():

    city = "Braunschweig"
    weather_dict = {}
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q=London&aqi=no"
    res = requests.get(url).json()
    if res is None:
        return None
    weather = res["data"]["list"][0]
    weather_dict[city] = [weather["weather"], weather["temp"],
                          weather["low"], weather["high"]]  # 天气，温度， 最低温，最高温
    return weather_dict

print(get_weather())