#get the pic of the food
from serpapi import GoogleSearch
import json
#return the first picture of the food
def get_foodpic(food: str) -> str:
    params = {
    "engine": "google",
    "location": "Germany",
    "q": f"{food}",
    "api_key": "6c54213a28cb3527f4fff27fd046d03eff8dfe64a0ddd2066df38c264651a631"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results["organic_results"]
    # print(json.dumps(organic_results, indent=4))

    # with open("rwa.json",'r',encoding='utf-8') as f:
    #     organic_results = json.loads(f.read())
    #     print(json.dumps(organic_results, indent=4))

    thumbnail = []
    text_template = ""
    for i in range(len(organic_results)):
        if "thumbnail" in organic_results[i].keys():
            thumbnail.append(organic_results[i]["thumbnail"])
    
    if len(thumbnail) > 1:
        text_template = "<img src={}> or <img src={}>".format(thumbnail[0],thumbnail[1])
    elif len(thumbnail) == 1:
        text_template = "<img src={}>".format(thumbnail[0])
    else:
        text_template = "No Picture"
    print(text_template)
    return text_template

if __name__ == "__main__":
    # with open("rwa.json",'r',encoding='utf-8') as f:
    #     organic_results = json.loads(f.read())
    #     print(organic_results[0]["thumbnail"])
    print(get_foodpic("food"))
