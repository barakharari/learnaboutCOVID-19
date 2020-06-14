import csv
import utilities as uts

def getUSInformation():

    usRates = []
    mostRecentDate = None

    with open('./covid-19-data/us.csv') as usCSV:
        reader = reversed(list(csv.reader(usCSV, delimiter = ',')))
        flag = True
        for line in reader:
            if flag:
                mostRecentDate = line[0]
                usRates.append((int(line[1]), int(line[2])))
                flag = False
            elif line[0] != mostRecentDate:
                usRates.insert(0, (int(line[1]), int(line[2])))
                break

    print(uts.updateStringWithRates("The rate of recorded coronavirus cases across the nation has ", usRates))
    uts.numberOfCasesAndDeathsAsOf(mostRecentDate, usRates[1][0], usRates[1][1])

def getStateInformation(state):

    stateRates = []
    mostRecentDate = None

    with open('./covid-19-data/us-states.csv') as statesCSV:
        reader = reversed(list(csv.reader(statesCSV, delimiter = ',')))
        flag = True
        for line in reader:
            if flag and str(line[1]) == state:
                mostRecentDate = line[0]
                stateRates.append((int(line[3]), int(line[4])))
                flag = False
            elif line[0] != mostRecentDate and str(line[1]) == state:
                stateRates.insert(0, (int(line[3]), int(line[4])))
                break

    print(uts.updateStringWithRates("The rate of recorded coronavirus cases in " + state + " has ", stateRates))
    uts.numberOfCasesAndDeathsAsOf(mostRecentDate, stateRates[1][0], stateRates[1][1])


def getCountyInformation(state, county):

    countyRates = []
    mostRecentDate = None

    with open('./covid-19-data/us-counties.csv') as countyCSV:
        reader = reversed(list(csv.reader(countyCSV, delimiter = ',')))
        flag = True
        for line in reader:
            if flag and str(line[2]) == state and str(line[1]) == county:
                mostRecentDate = line[0]
                countyRates.append((int(line[4]), int(line[5])))
                flag = False
            elif str(line[0]) != mostRecentDate and str(line[2]) == state and str(line[1]) == county:
                countyRates.insert(0,(int(line[4]), int(line[5])))
                break

    print(uts.updateStringWithRates("The rate of recorded coronavirus cases in " + county + ", " + state + " has ", countyRates))
    uts.numberOfCasesAndDeathsAsOf(mostRecentDate, countyRates[1][0], countyRates[1][1])
