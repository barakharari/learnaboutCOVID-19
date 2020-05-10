from textblob import TextBlob

def processInput(input):
    resultDict = {}
    input = TextBlob(input)
    print(input.words)
    return resultDict
