import requests

# id list
id_list = {"ostfalia_mensa": "130"}

# get menu from web api
def get_tages_menu(id, isoDate):
    url = "https://sls.api.stw-on.de/v1/locations/{id}/menu/{isoDate}".format(id=id, isoDate=isoDate)
    print("Sendding request: " + url)
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
  print(get_tages_menu("130", "2022-05-03"))
