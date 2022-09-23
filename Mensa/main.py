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

def get_week_day():
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    week_day = week_list[datetime.date(
        datetime.strptime(today, "%Y-%m-%d %H:%M:%S")).weekday()]
    return week_day

def run():
    pusher = WxPusher()
    content = ""
    menu = Mensa.pull_mensa_menu()
    week_day = time.strftime("%A", time.localtime()) 
    # template = open("template.html",encoding='UTF-8').read()
    content_format = f"""
    <div align="center">
        <h1>Thank you for the subscribe</h1>
    </div>
    <hr><b>Today is:</b>
    <font color={random_color()}>{week_day}</font>

    <hr>
    <b>Today's Menu: </b>
    <font color={random_color()}>{menu}</font>
    <hr>
    <div align="center">
        <h1>guten Appetit 😋</h1>
    </div>
    """
    
    pusher.send_message(content = content_format ,uids = uids,token = token)


    

    # push.send_message(content=contents, uids=uids, token=token)
    
if __name__ == "__main__":
    run()
