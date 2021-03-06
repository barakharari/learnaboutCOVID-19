import requests
import random
import json

def binarySearch(data, searchValue, low, high):
    if high < low:
        return []
    mid = int((low + high) / 2)
    if data[mid] < searchValue:
        return binarySearch(data, searchValue, mid, high)
    elif data[mid] > searchValue:
        return binarySearch(data, searchValue, low, mid)
    else:
        return data[mid]

def updateStringWithRates(startString, ratesArray):
    if len(ratesArray) == 2:
        rate = "{:.2f}".format(round((abs(ratesArray[1][0] - ratesArray[0][0])) / ratesArray[0][0]  * 100 , 2))
        if ratesArray[0][0] > ratesArray[1][0]:
             startString += "dropped by " + rate + "% "
        elif ratesArray[0][0] < ratesArray[1][0]:
             startString += "risen by " + rate + "% "
        else:
             startString += "not changed "
    else:
        startString = "Sorry, we cannot give accurate US coronavirus data at this moment"

    return startString

def numberOfCasesAndDeathsAsOf(day, cases, deaths):
    if cases != None and deaths != None:
        print("Number of cases as of " + day + ": " + str(cases))
        print("Number of deaths as of " + day + ": " + str(deaths))

#FUN FACTS
def getFunFact():
    with open('./covid19facts.txt') as funFacts:
        factIndex = random.randint(1, 55)
        info = []
        index = 0
        for line in funFacts:
            if (index == factIndex):
                info = line.split("~")
                break
            index += 1
        return "'" + info[0] + "' - " + info[1].strip()
    return None

#NEWS ARTICLES
def getRandomArticle():
    requestUrl = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=covid19&api-key=Ot0YWlwrcfzzV9e0Zc7lA02D1bylRP4D"
    response = requests.get(requestUrl)
    json_data = json.loads(response.text)["response"]

    randomArticleIndex = random.randint(0, len(json_data["docs"]))

    articleAbstract = json_data["docs"][randomArticleIndex]["abstract"]
    articleURL = json_data["docs"][randomArticleIndex]["web_url"]

    return (articleAbstract, articleURL)
