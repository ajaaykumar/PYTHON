""" 
Write a program to find the first non-repeated character in a string
"""

def first_non_rep_char(input_str):
  dict = {}
  for i,char in enumerate(input_str):
    if char not in dict:
      dict[char] = 1
    else:
      dict[char] += 1
  min_count = 1
  min_char = None
  for key,value in dict.items():
    if value == min_count:
      min_count = value
      min_char = key
      break
  return min_char

non_rep_char = first_non_rep_char("hello")
non_rep_char1 = first_non_rep_char("aab")
non_rep_char2 = first_non_rep_char("abcdabcd")
non_rep_char3 = first_non_rep_char("abcdeabcde")
non_rep_char4 = first_non_rep_char("abcdefghijklmnopqrstuvwxyz")

assert non_rep_char == 'h' , f"Value {non_rep_char} is not the first non-repeated character."
assert non_rep_char1 == 'b' , f"Value {non_rep_char1} is not the first non-repeated character."
assert non_rep_char2 == None , f"Value {non_rep_char2} is not the first non-repeated character."
assert non_rep_char3 == None , f"Value {non_rep_char3} is not the first non-repeated character."
assert non_rep_char4 == 'a' , f"Value {non_rep_char4} is not the first non-repeated character."



