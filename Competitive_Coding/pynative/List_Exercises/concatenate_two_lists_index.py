# Exercise Question 2: Concatenate two lists index-wise

def main(lst1,lst2):
    result = []
    for index,data in enumerate(lst1):
        result.append(data+lst2[index])

    return result

if __name__ == '__main__':
    list1 = ["M", "na", "i", "Ke"] 
    list2 = ["y", "me", "s", "lly"]
    main(list1,list2)




