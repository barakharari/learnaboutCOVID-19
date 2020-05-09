import csv
import datetime


def getUSInformation():
    yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
    dayBefore = str(datetime.date.today() - datetime.timedelta(days=2))
    usRates = []
    usDataMessage = ""

    with open('./covid-19-data/us.csv') as usCSV:
        reader = csv.reader(usCSV, delimiter = ',')
        for line in reader:
            if str(line[0]) == dayBefore or str(line[0]) == yesterday:
                usRates.append((int(line[1]), int(line[2])))


    if len(usRates) == 2:
        usDataMessage = "The rate of recorded coronavirus cases across the nation has "
        rate = "{:.2f}".format(round((usRates[1][0] - usRates[0][0]) * 100 / usRates[0][0], 2))
        if usRates[0][0] > usRates[1][0]:
             usDataMessage += "dropped by " + rate + "% "
        elif usRates[0][0] < usRates[1][0]:
             usDataMessage += "risen by " + rate + "% "
        else:
            usDataMessage += "not changed "

        usDataMessage += "since yesterday"
    else:
        usDataMessage = "Sorry, we cannot give accurate coronavirus data at this moment"


    return usDataMessage

# def getStateInformation():
