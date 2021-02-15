# Exercise Question 5: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order

def main(list1,list2):
    for index,num in enumerate(list1, start=1):
        print(num,list2[len(list2)-index])

if __name__ == '__main__':
    lst1 = [10, 20, 30, 40]
    lst2 = [100, 200, 300, 400]    
    main(lst1,lst2)




