# Exercise Question 6: Remove empty strings from the list of strings

def main(lst):
    for index,num in enumerate(lst):
        if len(num) < 1:
            lst.pop(index)
    print(lst)

if __name__ == '__main__':
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    main(list1)





