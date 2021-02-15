# Exercise Question 9: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

def main(lst):
    index_val = lst.index(20)
    lst.insert(index_val,200)
    print(lst)

if __name__ == "__main__":
    list1 = [5, 10, 15, 20, 25, 50, 20]
    main(list1)

