import info as info
import random
import requests
import json
import handleInput as hI
from twilio.rest import Client

input = "How many cases in Broome, New York?"

# processed = hI.processInput(input)

#CASE/DEATH/RATE INFORMATION
info.getUSInformation()
info.getStateInformation("Ohio")
info.getCountyInformation("Ohio", "Lorain")

#FUN FACTS
with open('./covid19facts.txt') as funFacts:
    factIndex = random.randint(1, 55)
    info = []
    index = 0
    for line in funFacts:
        if (index == factIndex):
            info = line.split("~")
            break
        index += 1
    print("'" + info[0] + "' - " + info[1].strip())

#NEWS ARTICLES
requestUrl = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=covid19&api-key=Ot0YWlwrcfzzV9e0Zc7lA02D1bylRP4D"
response = requests.get(requestUrl)
json_data = json.loads(response.text)["response"]

randomArticleIndex = random.randint(0, len(json_data["docs"]))

articleAbstract = json_data["docs"][randomArticleIndex]["abstract"]
articuleURL = json_data["docs"][randomArticleIndex]["web_url"]

print(articleAbstract)
