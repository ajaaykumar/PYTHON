# dictionary exercise 10: Given a Python dictionary, Change Brad’s salary to 8500
def main(sampleDict,name):
    for key,value in sampleDict.items():
        if value["name"] == name:
            value["salary"] = 8500
    print(sampleDict)

if __name__ == '__main__':
    sampleDict = {'emp1': {'name': 'Jhon', 'salary': 7500},'emp2': {'name': 'Emma', 'salary': 8000},'emp3': {'name': 'Brad', 'salary': 6500}}
    name = "Brad"
    main(sampleDict,name)