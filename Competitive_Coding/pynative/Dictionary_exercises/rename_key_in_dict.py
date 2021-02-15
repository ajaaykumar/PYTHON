# dictionary exercise 8: Rename key city to location in the following dictionary

def main(sampleDict, name):
    sampleDict[name] = sampleDict["city"]
    del sampleDict["city"]
    print(sampleDict)


if __name__ == '__main__':
    sampleDict = {"name":"Kelly","age":25,"salary":8000,"city":"New york"}
    name = 'location'
    main(sampleDict, name)




