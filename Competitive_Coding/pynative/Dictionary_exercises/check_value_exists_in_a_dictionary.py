# dictionary exercise 7: Check if a value 200 exists in a dictionary

def main(sampleDict, value):
    if value in sampleDict.values():
        print(True)

if __name__ == '__main__':
    sampleDict = {'a': 100, 'b': 200, 'c': 300}
    value = 200
    main(sampleDict, value)



