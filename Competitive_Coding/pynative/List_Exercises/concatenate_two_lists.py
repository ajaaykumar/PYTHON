# Exercise Question 4: Concatenate two lists in the following order


def main(list1,list2):
    result = []
    for i in list1:
        for j in list2:
            result.append(i+j)
    print(result)

if __name__ == '__main__':
    lst1 = ["Hello ", "take "]
    lst2 = ["Dear", "Sir"]
    main(lst1,lst2)
