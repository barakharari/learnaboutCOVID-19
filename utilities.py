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
        rate = "{:.2f}".format(round((ratesArray[1][0] - ratesArray[0][0]) * 100 / ratesArray[0][0], 2))
        if ratesArray[0][0] > ratesArray[1][0]:
             startString += "dropped by " + rate + "% "
        elif ratesArray[0][0] < ratesArray[1][0]:
             startString += "risen by " + rate + "% "
        else:
             startString += "not changed "

        startString += "since yesterday"
    else:
        startString = "Sorry, we cannot give accurate US coronavirus data at this moment"

    return startString

def numberOfCasesAndDeathsAsOf(day, cases, deaths):
    if cases != None and deaths != None:
        print("Number of cases as of " + day + ": " + str(cases))
        print("Number of deaths as of " + day + ": " + str(deaths))
