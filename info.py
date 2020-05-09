import csv
import datetime
import utilities as uts

yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
dayBefore = str(datetime.date.today() - datetime.timedelta(days=2))

def getUSInformation():

    usRates = []

    with open('./covid-19-data/us.csv') as usCSV:
        reader = csv.reader(usCSV, delimiter = ',')
        for line in reader:
            if str(line[0]) == dayBefore or str(line[0]) == yesterday:
                usRates.append((int(line[1]), int(line[2])))

    print(uts.updateStringWithRates("The rate of recorded coronavirus cases across the nation has ", usRates))
    uts.numberOfCasesAndDeathsAsOf(yesterday, usRates[1][0], usRates[1][1])

def getStateInformation(state):

    stateRates = []

    with open('./covid-19-data/us-states.csv') as statesCSV:
        reader = csv.reader(statesCSV, delimiter = ',')
        for line in reader:
            if (str(line[0]) == dayBefore or str(line[0]) == yesterday) and str(line[1]) == state:
                stateRates.append((int(line[3]), int(line[4])))

    print(uts.updateStringWithRates("The rate of recorded coronavirus cases in " + state + " has ", stateRates))
    uts.numberOfCasesAndDeathsAsOf(yesterday, stateRates[1][0], stateRates[1][1])


def getCountyInformation(state, county):

    countyRates = []

    with open('./covid-19-data/us-counties.csv') as countyCSV:
        reader = csv.reader(countyCSV, delimiter = ',')
        for line in reader:
            if (str(line[0]) == dayBefore or str(line[0]) == yesterday) and str(line[2]) == state and str(line[1]) == county:
                countyRates.append((int(line[4]), int(line[5])))

    print(uts.updateStringWithRates("The rate of recorded coronavirus cases in " + county + ", " + state + " has ", countyRates))
    uts.numberOfCasesAndDeathsAsOf(yesterday, countyRates[1][0], countyRates[1][1])
