# Exercise Question 7: Add item 7000 after 6000 in the following Python List

def add_item(lst):
    lst[2][2].append(7000)
    print(lst)

if __name__ == '__main__':
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    add_item(list1)






