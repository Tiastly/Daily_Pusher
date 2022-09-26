import requests
import json
import datetime

# mensa id list 
id_list = {"ostfalia_mensa": "130"}
# get isoDate from today
today = datetime.date.today()

def get_tages_menu(id: str, isoDate: str) -> dict:
    r"""Get menu from mensa Web API.

    :param id: Die ID der Mensa. Siehe Liste aller Mensen: https://api.stw-on.de/#liste-aller-mensen
    :param isoDate: Datum nach ISO 8601 (z.B. 2020-06-18)
    :return: dict of  menu.
    """
    url = f"https://sls.api.stw-on.de/v1/locations/{id}/menu/{isoDate}"
    print("Sendding request: " + url)
    r = json.loads(requests.get(url).text)
    return r

def get_menu_count(menus: dict) -> int:
    r"""Get the number of menus.

    :param menus: The menu dict from get_tages_menu().
    :return: The number of menus.
    """
    return len(menus["meals"])

def get_menu_name(menus: dict) -> list:
    r"""Get menu name from menu dict.

    :param menus: dict from get_tages_menu().
    :return: list that includes the menu name.
    """
    menu_names = []
    for menu in menus["meals"]:
        menu_names.append(menu["name"])
    return menu_names

def get_menu_foodtype(menus: dict) -> list:
    r"""Get food type from menu dict.

    :param menus: dict from get_tages_menu().
    :return: list of food type.
    """
    menu_prices = []
    for menu in menus["meals"]:
        menu_prices.append(menu["price"]["student"])
    return menu_prices

def get_menu_price(menus: dict) -> list:
    r"""Get menu price from menu dict.

    :param menus: dict from get_tages_menu().
    :return: list of menu price.
    """
    menu_prices = []
    for menu in menus["meals"]:
        menu_prices.append(menu["price"]["student"])
    return menu_prices

def get_menu_nutritional_values(menus: dict) -> list:
    r"""Get menu nutritional values per 100 gram from menu dict.

    :param menus: dict from get_tages_menu().
    :return: list of dict that includes the menu nutritional values include:
             {caloric_value} {fat} {saturated_fatty_acids} {carbohydrates} {sugar} {roughage} {protein} {salt}
    """
    menu_nutritional_values = []
    for menu in menus["meals"]:
        menu_nutritional_values.append(menu["nutritional_values"]["per_100_grams"])
    return menu_nutritional_values


if __name__ == "__main__":
  dic = get_tages_menu(id_list["ostfalia_mensa"], today)
  print(get_menu_count(dic))
  print(get_menu_name(dic))
  print()
  print(get_menu_price(dic))
  print(get_menu_nutritional_values(dic))
