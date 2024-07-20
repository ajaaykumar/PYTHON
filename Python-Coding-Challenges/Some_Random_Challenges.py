# Write a program to find the first non-repeated character in a string
# Write a program to check if two strings are anagrams of each other
# Write a program to find the longest substring without repeating characters
# Write a program to find the longest common prefix among a set of strings
# Write a program to remove a specific character from a string
# Write a program to implement the Rabin-Karp algorithm for string matching
# Write a program to convert a string to its equivalent integer
# Write a program to replace a specific word in a string with another word.



# what is the best way to loop an list without using for loop
my_list = [1, 2, 3, 4, 5]
# create an iterator object
iterator = iter(my_list)

# use the iterator in a while loop
while True:
    try:
        # get the next item from the iterator
        item = next(iterator)
        print(item)
    except StopIteration:
        # exit the loop when the iterator is exhausted
        break


# Convert intiger to string using mathematical equation
def intTostr(s):
  digits = '0123456789'
  result = ''
  if s == 0:
    result = '0'
  while s > 0:
    result = digits[s%10] + result
    s = s//10

  return result









