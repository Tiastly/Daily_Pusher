import MensaAPI as mensa
from CuteCat import *
import time

bot = CuteCat( api_url = 'http://127.0.0.1:8090' , robot_wxid = 'wxid_8xyxdxd49tbp22')

def at_me(msg)->bool:
    if 'wxid=wxid_8xyxdxd49tbp22' in msg['msg'] and '@at' in msg['msg']:
        return True
    else:
        return False

def trigger(msg, trigger_word:str)->bool:
    if trigger_word in msg['msg']:
        return True
    else:
        return False


# @bot.on('EventFriendMsg')
# def eventfrinendmsg(msg):
#     print(msg)
#     if msg['msg'] == '嘉然今天吃什么':
#         menus = mensa.get_tages_menu(mensa.id_list["ostfalia_mensa"], mensa.today)
#         bot.SendTextMsg(to_wxid= msg.from_wxid, msg = str(mensa.get_menu_name(menus)))

# @bot.on('EventGroupMsg')
# def eventgroupmsg(msg):
#     print(msg)
#     if msg['msg'] == '嘉然今天吃什么':
#         menus = mensa.get_tages_menu(mensa.id_list["ostfalia_mensa"], mensa.today)
#         bot.SendTextMsg(to_wxid= msg.from_wxid, msg = str(mensa.get_menu_name(menus)))


@bot.on('EventGroupMsg')
# Priority: 10
def ping(msg):
    print(msg)
    # 严格等于
    if msg['msg'] == '[@at,nickname=食堂大妈,wxid=wxid_8xyxdxd49tbp22]  ':
      bot.SendTextMsg(to_wxid= msg.from_wxid, msg = "什么事小伙子")

@bot.on('EventGroupMsg')
# Priority: 1
def pull_mensa_menu(msg):
    print(msg)
    if at_me(msg) and trigger(msg, "菜单"):
        bot.SendTextMsg(to_wxid= msg.from_wxid, msg = "小伙子别急,今天的菜单马上来")
        time.sleep(2)
        menus = mensa.get_tages_menu(mensa.id_list["ostfalia_mensa"], mensa.today)
        format_text = ""
        name = mensa.get_menu_name(menus)
        price = mensa.get_menu_price(menus)
        nutritional_values = mensa.get_menu_nutritional_values(menus)
        # bot.SendTextMsg(to_wxid= "20479741621@chatroom", msg = "[@emoji=\uD83C\uDF1F]Mensa今天的菜单是：")
        for i in range(mensa.get_menu_count(menus)):
            format_text +=  str(i+1) + ". " + name[i] + "\n" +\
                            "- 学生价: " + str(price[i]) + "欧" + "\n" +\
                            "- 热量(/100g): " + str(nutritional_values[i]["caloric_value"])
                            # "- 脂肪(/100g): " + str(nutritional_values[i]["fat"]) + "\n" +\
                            # "- 碳水(/100g): " + str(nutritional_values[i]["carbohydrates"]) + "\n" +\
                            # "- 糖份(/100g): " + str(nutritional_values[i]["sugar"]) + "\n" +\
                            # "- 蛋白质(/100g): " + str(nutritional_values[i]["protein"]) + "\n" +\
            bot.SendTextMsg(to_wxid= msg.from_wxid, msg = format_text)
            format_text = ""
            time.sleep(1)
        # bot.SendTextMsg(to_wxid= msg.from_wxid, msg = "")

bot.run()

# TODO: 1.关键词字典触发