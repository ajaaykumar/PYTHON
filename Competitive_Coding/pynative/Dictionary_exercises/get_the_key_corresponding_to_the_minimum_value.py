# dictionary exercise 9: Get the key corresponding to the minimum value from the following dictionary

def main(sampleDict):
    samp = list(sampleDict.values())
    min_value = samp[0]
    for val in samp:
        if min_value > val:
            min_value = val
    print(min_value)


if __name__ == '__main__':
    sampleDict = {'Physics': 82,'Math': 65,'history': 75}
    main(sampleDict)
