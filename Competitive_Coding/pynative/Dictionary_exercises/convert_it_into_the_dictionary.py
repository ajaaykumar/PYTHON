# dictionary exercise 1: Below are the two lists convert it into the dictionary


def main(_key,_value):
    result = {}
    for index, values in enumerate(_key):
        result[values] = _value[index]
    print(result)

if __name__ == "__main__":
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]    
    main(keys,values)



