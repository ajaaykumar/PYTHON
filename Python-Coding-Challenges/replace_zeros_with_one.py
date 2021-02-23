"""Question 2. Write a Program to replace all 0’s with 1 in a given integer.

Given an integer as an input, all the 0’s in the number has to be replaced with 1.

For example, consider the following number

Input: 102405
Output: 112415

Input: 56004
Output: 56114"""


def replaceValue():
    nums = 102405
    nums = list(str(nums))
    # rep = nums.replace('0','1')
    
    # print(int(rep))

    for index,element in enumerate(nums):
        if int(element) == 0:
            nums[index] = 1
    
    result = "".join([str(i) for i in nums])
    print(result)
    
replaceValue()

"""
Q.Given a string convert it into compressed form.
Sample 1
Input-ppaaatts
Output-p2a3t2s1

In case length of output is greater than length of input give input as output

Sample 2
Input -abcde
Output-abcde

Since a1b1c1d1e1    length is greater than length of input."""



