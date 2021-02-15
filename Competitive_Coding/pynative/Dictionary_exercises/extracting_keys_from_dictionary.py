# dictionary exercise 5: Create a new dictionary by extracting the following keys from a given dictionary
def main(sampleDict, keys):
    result = {}
    for key in keys:
        if key in sampleDict:
            result[key]=sampleDict[key]
    
    print(result)

    # print({k:sampleDict[k] for k in keys})

if __name__ == '__main__':
    sampleDict = {"name":"Kelly","age":25,"salary":8000,"city":"New york"}
    Keys_to_extract = ["name", "salary"]
    main(sampleDict, Keys_to_extract)


