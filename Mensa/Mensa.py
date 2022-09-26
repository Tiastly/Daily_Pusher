# mensa text
import MensaAPI as mensa
from Pictures import *
# from Translate import *
# import time

def pull_mensa_menu():

    menus = mensa.get_tages_menu(mensa.id_list["ostfalia_mensa"], mensa.today)
    text = ""
    name = mensa.get_menu_name(menus)
    lena = mensa.get_menu_lane(menus)
    price = mensa.get_menu_price(menus)
    nutritional_values = mensa.get_menu_nutritional_values(menus)
    for i in range(mensa.get_menu_count(menus)):
        text +=  str(i+1) + ". " +  name[i] + "\n" +\
                        "- 学生价: " + str(price[i]) + "欧" + "\n" +\
                        "- 热量(/100g): " + str(nutritional_values[i]["caloric_value"])+'\n'
                        # "- "+translate_raw_text_zh(name[i]) + '\n' +\
        if "Essen" in lena[i] :
            text += get_foodpic(name[i]) + '\n'
    #     # format_text +=  str(i+1) + ". " + translate_raw_text_zh(name[i]) + name[i] + "\n" +\
    #     #                 "- 学生价: " + str(price[i]) + "欧" + "\n" +\
    #     #                 "- 热量(/100g): " + str(nutritional_values[i]["caloric_value"])

    #                     # "- 脂肪(/100g): " + str(nutritional_values[i]["fat"]) + "\n" +\
    #                     # "- 碳水(/100g): " + str(nutritional_values[i]["carbohydrates"]) + "\n" +\
    #                     # "- 糖份(/100g): " + str(nutritional_values[i]["sugar"]) + "\n" +\
    #                     # "- 蛋白质(/100g): " + str(nutritional_values[i]["protein"]) + "\n" +\
    
    # print(text)
    return text