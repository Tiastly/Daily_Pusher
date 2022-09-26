import Mensa
from wxpusher import WxPusher
import time
# from datetime import datetime, timedelta
import random
token = "AT_fTLp0Wb5B2v1TxpGjGLAtP3PX1JdtNIz" #app token
uids = ["UID_HblsALCQJ5YkAWIJcmJMuhPqDmn8"] #subscribe
# TOPIC_IDS = [ '7526']

def random_color():
    color_code = "0123456789ABCDEF"
    color_str = ""
    for num in range(6):
        color_str += random.choice(color_code)
    return color_str

def run():
    pusher = WxPusher()
    content = ""
    menu = Mensa.pull_mensa_menu()
    week_day = time.strftime("%A", time.localtime()) 
    if menu == None:
        endword = "Schönes Wochenende 😉"
    else:
        endword = "guten Appetit 😋"
    # template = open("template.html",encoding='UTF-8').read()
    content_format = f"""
    <div align="center">
        <h1>Thank you for the subscribe 💖</h1>
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
    
    pusher.send_message(content = content_format ,uids = uids,token = token)

    # push.send_message(content=contents, uids=uids, token=token)
    
if __name__ == "__main__":
    run()
