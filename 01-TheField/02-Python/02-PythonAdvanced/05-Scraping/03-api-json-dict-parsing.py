import requests
import json

"""
root_url = "https://newsapi.org/v2"
endpoint = "top-headlines" 
params = {
    "apiKey": "73bbb95f8ecb49b499113a46481b4af1",
    "sources": "lequipe"
}

# call the get method of requests on our specifications
response = requests.get(f"{root_url}/{endpoint}", params=params)
x = response.json() # --- return a dict
# ----------------------- can only write a str

data = "./api-data.json"
with open(data, "w", encoding="utf-8") as data: ## --- with open(data, "w") as data:
    json.dump(x, data, indent=4) ## --------------------- data.write(x)
"""

# clean the JSON response here

file = "./api-data.json"
with open(file, "r", encoding="utf-8") as data:
    content = json.load(data)
    
# data = "api-data.txt"
# with open(data, "r") as data:
#     content = data.read()

pretty_json = json.dumps(content["articles"][5], indent=4) # dict into a indent str

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

print("#--------------------------------------------------------")
print("#--------- keys, total result, status, articles ---------")
print("#--------------------------------------------------------")
print(f"content keys: {content.keys()}")
print(f"total Results: {content["totalResults"]}")
print(f"request status: {content["status"]}")
print("#--------------------------------------------------------")
print(f"author: {content["articles"][0]["author"]}")
print(f"source: {content["articles"][0]["source"]}") # again a dict (a small one)
print(f"title: {content["articles"][0]["title"]}")
print(f"published at: {content["articles"][0]["publishedAt"]}")
print("#--------------------------------------------------------")
print("#-------------- Titre des articles ----------------------")
print("#--------------------------------------------------------")

i = 0
articles = []
for x in content["articles"][i]:
    articles.append(content["articles"][i]["title"])
    i += 1

for i in range(len(articles)):
    print(articles[i])

print("#--------------------------------------------------------")
print("#-------------- short description ----------------------")
print("#--------------------------------------------------------")

i = 0
descr = []
for x in content["articles"][i]:
    descr.append(content["articles"][i]["description"])
    i += 1

for i in range(len(descr)):
    print(descr[i][:128]) # only the first 128 char.

print("#--------------------------------------------------------")
print("#------------- Article[0] keys --------------------------")
print("#--")

print(f"--- articles[0].keys: {content["articles"][0].keys()}")

print("#--")
print("#--------------json content[5] --------------------------")
print("#--------------------------------------------------------")
print(pretty_json) # type = str