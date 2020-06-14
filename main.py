import info as info
import utilities as ut

userInput = None
flag = False

def usage():
    print()
    print("  USAGE:")
    print("\tFor US information type: 'US'")
    print("\tFor state information type: '<state>'")
    print("\tFor county information type: '<state>, <county>'")
    print("\tFor random coronavirus fact type: 'FF'")
    print("\tFor NYTimes article regarding coronavirus type: 'NYT'")
    print("\tType 'exit' to exit program")
    print("\tType 'options' to see these options again")

def handleInput(inp):
    str = ""
    inp = inp.split()
    for i in inp: str += i.capitalize() + " "
    return str.strip()

usage()

while(True):
    print()
    if not flag:
        userInput = input("What do you wanna see today? ")
        flag = True
    else: userInput =  input("Anything else? ")

    userInput = userInput.split(',')

    if len(userInput) == 1:
        text = userInput[0].lower()
        if text == "exit": break
        elif text == "options": usage()
        elif text == "us":
            print("\n----US INFORMATION----\n")
            info.getUSInformation()
        elif text == "ff":
            print("\n----FUN FACT----\n")
            ff = ut.getFunFact()
            if ff is not None: print(ff)
            else: print("Sorry, no fun fact available at this time")
        elif text == "nyt":
            print("\n----RANDOM ARTICLE----\n")
            article = ut.getRandomArticle()
            if article is not None:
                print("HEADLINE: " + article[0])
                print()
                print("URL: " + article[1])
                print()
        else:
            print("\n----" + userInput[0].upper().strip() + " INFORMATION----\n")
            info.getStateInformation(handleInput(userInput[0]))
    else:
        print("\n----" + userInput[0].upper().strip() + "," + userInput[1].upper().strip() + " INFORMATION----\n")



        info.getCountyInformation(handleInput(userInput[0]), handleInput(userInput[1]))
