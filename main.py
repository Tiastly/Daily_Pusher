import Mensa
from wxpusher import WxPusher

import time
import random
import json

token = "AT_fTLp0Wb5B2v1TxpGjGLAtP3PX1JdtNIz" #app token
# uids = ["UID_HblsALCQJ5YkAWIJcmJMuhPqDmn8"] #subscribe
TOPIC_IDS = [ '7526']

pusher = WxPusher()

def random_color() -> str:
    color_code = "0123456789ABCDEF"
    color_str = ""
    for _ in range(6):
        color_str += random.choice(color_code)
    return color_str

def run():
    pusher = WxPusher()
    def get_uids(WxPusher:pusher) -> list:
        uids = set()
        users = pusher.query_user(page = 1,page_size = 20,token = token)
        for i in range(len(users['data']['records'])):
            uids.add(users['data']['records'][i]['uid'])
        return list(uids)

    content = ""
    uids = get_uids(pusher)

    menu = Mensa.pull_mensa_menu()
    week_day = time.strftime("%A", time.localtime()) 

    if len(menu) == 0:
        endword = "Schönes Wochenende 😉"
    else:
        endword = "guten Appetit 😋"
    # template = open("template.html",encoding='UTF-8').read()

    content_format = f"""
    <div align="center">
        <h1>✨ Thank you for the subscribe ✨</h1>
    </div>
    <hr><b>Today is:</b>
    <font color={random_color()}>{week_day}</font>

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

    # push.send_message(content=contents, uids=uids, token=token)
    
if __name__ == "__main__":
    run()

