# Exercise Question 3: Given a Python list. Turn every item of a list into its square

def solve(lst):
    for index,num in enumerate(lst):
        lst[index] = num*num
            
    print(lst)
        

if __name__ == '__main__':
    aList = [1, 2, 3, 4, 5, 6, 7]
    solve(aList)


