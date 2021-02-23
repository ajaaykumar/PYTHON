# Given an array of integers in ascending order, return index of the two numbers such that they add up to a specific key provided.
# Example:
# Take the array [1,2,3,4] and “key” is 7.
def checkSum(array,key):
    for index,num in enumerate(array):
        for nested_val in array[index+1:-1]:
            if num + nested_val == key:
                print(index,array.index(nested_val))

array = [1,2,3,4,5] 
key =  7
checkSum(array,key)