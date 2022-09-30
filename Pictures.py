#pic of the food module
from serpapi import GoogleSearch
import json
import os

def get_foodpic(food: str) -> str:
    r'''
    search food pictures from google.

    :param food: search keyword.
    :return: the first and second thumbnail of the food
    '''
    key = os.getenv("pic_key")
    params = {
    "engine": "google",
    "location": "Germany",
    "q": f"{food}",
    "api_key":f"{key}",
    }
    
    organic_results = []
    # 每个月100次谨慎使用
    # search = GoogleSearch(params)
    # results = search.get_dict()
    # organic_results = results["organic_results"]

    # print(json.dumps(organic_results, indent=4))


    thumbnail = []
    text_template = ""
    for item in organic_results:
        if "thumbnail" in item.keys():
            thumbnail.append(item["thumbnail"])
    
    if len(thumbnail) > 1:
        text_template = "<img src={}> or <img src={}>".format(thumbnail[0],thumbnail[1])
    elif len(thumbnail) == 1:
        text_template = "<img src={}>".format(thumbnail[0])
    else:
        text_template = "No Picture"

    print(text_template)

    
    return text_template

if __name__ == "__main__":
    print(get_foodpic("food"))
