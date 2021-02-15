# dictionary exercise 6: Delete set of keys from Python Dictionary
def main(sampleDict, keysToRemove):
    for i in keysToRemove:
        if i in sampleDict:
            del sampleDict[i]
    
    print(sampleDict)


if __name__ == '__main__':
    sampleDict = {"name":"Kelly","age":25,"salary":8000,"city":"New york"}
    keysToRemove = ["name", "salary"]
    main(sampleDict, keysToRemove)
