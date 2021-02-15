# Exercise Question 10: Given a Python list, remove all occurrence of 20 from the list

def removeValue(list1,val):
    return [i for i in list1 if i != val]

def main(lst):
    result = removeValue(lst,20)
    print(result)

    # for ind,value in enumerate(lst):
    #     if value==20:
    #         del lst[ind]
    # print(lst)





if __name__ == "__main__":
    list1 = [5, 10, 15, 20, 25, 50, 20]
    main(list1)

