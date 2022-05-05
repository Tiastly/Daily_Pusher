# 大妈作为Mensa机器人相关的函数

from Essential import *
import MensaAPI as mensa
from CuteCat import *
from Translate import *
import time

def pull_mensa_menu(bot: CuteCat, msg: dict) -> None:
    r"""拉取食堂今日菜单.

    :param bot: CuteCat实例
    :param msg: 消息字典
    :return: None
    """
    print(msg)
    bot.SendTextMsg(to_wxid= msg.from_wxid, msg = "小伙子别急,今天的菜单马上来")
    time.sleep(1)
    menus = mensa.get_tages_menu(mensa.id_list["ostfalia_mensa"], mensa.today)
    format_text = ""
    name = mensa.get_menu_name(menus)
    price = mensa.get_menu_price(menus)
    nutritional_values = mensa.get_menu_nutritional_values(menus)
    # bot.SendTextMsg(to_wxid= "20479741621@chatroom", msg = "[@emoji=\uD83C\uDF1F]Mensa今天的菜单是：")
    for i in range(mensa.get_menu_count(menus)):
        format_text +=  str(i+1) + ". " + translate_raw_text_zh(name[i]) + name[i] + "\n" +\
                        "- 学生价: " + str(price[i]) + "欧" + "\n" +\
                        "- 热量(/100g): " + str(nutritional_values[i]["caloric_value"])
                        # "- 脂肪(/100g): " + str(nutritional_values[i]["fat"]) + "\n" +\
                        # "- 碳水(/100g): " + str(nutritional_values[i]["carbohydrates"]) + "\n" +\
                        # "- 糖份(/100g): " + str(nutritional_values[i]["sugar"]) + "\n" +\
                        # "- 蛋白质(/100g): " + str(nutritional_values[i]["protein"]) + "\n" +\
        bot.SendTextMsg(to_wxid= msg.from_wxid, msg = format_text)
        format_text = ""
        time.sleep(1)