from wxpusher import WxPusher
from WeatherAPI import WeatherReport
import Mensa

import json
import random
import datetime
import os


token = os.getenv("wx_token") #app token
# uids = [os.getenv("wx_uids")] #subscribe
topicIds = [ '7526']

endingwords ={
    "NORMAL"  : "Guten Appetit 😋" ,
    "WEEKEND" : "Schönes Wochenende 😉",
    "HOLIDAY" : "No Work Today 😴",
    }

today = datetime.date.today()
week_day = today.strftime("%A") 

def random_color() -> str:
    color_code = "0123456789ABCDEF"
    color_str = ""
    for _ in range(6):
        color_str += random.choice(color_code)
    return color_str

def weather_module() -> str:
    wr = WeatherReport(today = today)
    weather_text = "{}°C - {}°C\n".format(wr.get_highest(),wr.get_lowest())+\
                    wr.get_weather_icon()
    return weather_text

def get_uids(pusher:WxPusher) -> list:
        uids = set()
        users = pusher.query_user(page = 1,page_size = 50,token = token)
        for item in users['data']['records']:
            uids.add(item['uid'])
        return list(uids)

def run():
    pusher = WxPusher()
    uids = get_uids(pusher)
    menu = Mensa.pull_mensa_menu()
    if week_day == 5 or week_day == 6:
        menu = "Today has no Menu"
        endword = endingwords['WEEKEND']
    elif not menu:
        menu = f"Das Mensa ist am {today} Geschlossen!"
        endword = endingwords['HOLIDAY']
    else:
        endword = endingwords['NORMAL']


    content_format = f"""
        <div align="center">
        <h1>✨ Thank you for the subscribe ✨</h1>
        </div>
        <hr><b>Today is:</b>
        <font color={random_color()}>{week_day}</font>

        <hr><b>Today's Weather in Braunschweig:</b>
        <font color={random_color()}>{weather_module()}</font>

        <hr>
        <b>Today's Menu: </b>
        <font color={random_color()}>{menu}</font>

        <hr>
        <div align="center">
            <h1>{endword}</h1>
        </div>
    """

    # applications
    pusher.send_message(content = content_format ,uids = uids ,token = token)
    # topic
    # pusher.send_message(content = content_format ,uids = uids ,token = token, topicIds=topicIds)

    # push.send_message(content=contents, uids=uids, token=token)
    print("Success!Check it in WeChat:)")

if __name__ == "__main__":
    run()