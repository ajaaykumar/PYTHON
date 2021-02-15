# dictionary exercise 2: Merge following two Python dictionaries into one

def main(dict1,dict2):
    for key,value in dict2.items():
        dict1[key] = value
    
    print(dict1)

if __name__ == "__main__":
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}  
    main(dict1,dict2)



