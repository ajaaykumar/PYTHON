
## 1. Basic Maths Logic Buildup
### Extraction of digits
1. Extraction of Digits using loops
    - Count Digits
    - Reverse a number

2. Count the Number of Digits in an Integer.
    

3. Check if a Number is **Palindrome**.
  - A palindrome is a word, phrase, number, or sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
    ```
        Number = 1221
        String = 'MADAM'
    ```
4. Check if a Number is **Armstrong Number**.
    ```
    153  = 1^3 + 5^3 + 3^3
            = 1 + 125 + 27
            = 153

    1634 = 1^4 + 6^4 + 3^4 + 4^4
            = 1 + 1296 + 81 + 256
            = 1634 
    ```
5. Print the **Factors** of a Given Number.
    ```
        10 -> [1,2,5,10]
        15 -> [1,2,5,10,15]
        25 -> [1,5,25]
        7  -> [1,7]
        19 -> [1,19]
    ```

6. Frequency Map/ Dictionary
    ```
        nums = [5,6,7,7,1,9,1]
        dict = {5:1, 6:1, 7:2, 1:2, 9:1}
    ```

## 2. Hashing
* Learn Basics of Hashing
* Count Frequency in a Range
* Highest / Lowest Frequency Elements: Frequency of the Most Frequent Element


## 3. Recursion Concept

### Introduction to Recursion Concept
* **Definition** : A function that calls itself.
* **Key Components** : 
    - **Base Case** : Stops recursion (e.g., if n == 0: return 1).
    - **Recursive Case** : Breaks the problem into smaller parts (e.g., return n * factorial(n-1)). 
    - **Call Stack** : Tracks function calls. Each recursive call adds a frame to the stack; when the base case is reached, the stack unwinds. 
    
1. What is Parameterized Recursion?
2. What is Functional Recursion?
3. Find the Factorial of a Number Using Recursion.
4. Reverse an Array Using Recursion.
5. Check if a String is Palindrome or Not Using Recussion.
6. Find the **Fibonacci Number** Using Recussion.
    <details>
        <summary>The Fibonacci Sequence is a series of numbers where: Each number is the sum of the two preceding ones, starting from 0 and 1.</summary>

        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
        F(n) = F(n-1) + F(n-2)

        with base conditions:
            F(0) = 0
            F(1) = 1
    </details>

## 4. Different Types of Sorting

### Selection Sort
1. Implement Selection Sort

    **Problem:**
    Given an unsorted array of integers, sort it using the Selection Sort algorithm.

    **Input:**
    ``` arr = [64, 25, 12, 22, 11] ```

    **Output:**
    ``` [11, 12, 22, 25, 64] ```
2. Sort in Descending Order Using Selection Sort

    **Problem:**
    Modify your selection sort to sort the array in descending order.

    **Input:**
    ```arr = [4, 1, 3, 9, 7]```

    **Output:**
    ```[9, 7, 4, 3, 1]```
    

3. Count Number of Swaps in Selection Sort

    **Problem:**
    Given an array, perform selection sort and return the total number of swaps done during the sorting.

    **Input:**
    ```arr = [5, 3, 4, 1, 2]```

    **Output:**
    ```2 (Only count the actual swaps made)```

4. Sort a List of Strings Alphabetically

    **Problem:**
    Given a list of strings, sort them in lexicographical order using selection sort.

    **Input:**
    ```arr = ["banana", "apple", "cherry", "date"]```

    **Output:**
    ```["apple", "banana", "cherry", "date"]```

    👉 Focus: Apply selection sort to non-numeric data by comparing strings.

5. Sort an Array of Tuples Based on Second Element

    **Problem:**
    Given a list of tuples, sort them by the second element using selection sort.

    **Input:**
    ```arr = [(1, 3), (2, 1), (4, 2)]```

    **Output:**
    ```[(2, 1), (4, 2), (1, 3)]```

    👉 Focus: Understand how to sort based on a key other than the default (like x[1]).

6. Stable Selection Sort

    **Problem:**
    Implement a stable version of selection sort. In normal selection sort, the algorithm is not stable (i.e., equal elements may switch their relative positions).

    **Input:**
    ```arr = [4, 5, 3, 4, 2]```

    Output (Stable Sort):
    ```[2, 3, 4 (first one), 4 (second one), 5]```

    👉 Focus: Instead of swapping, shift elements and insert the minimum at the correct position to maintain the original order.


7. Visualize Each Step of Selection Sort

    **Problem:**
    Print the array after each pass of selection sort to help visualize how the algorithm progresses.

    **Input:**
    ```arr = [29, 10, 14, 37, 13]```

    **Output:**
    ``` python
    Pass 1: [10, 29, 14, 37, 13]  
    Pass 2: [10, 13, 14, 37, 29]  
    Pass 3: [10, 13, 14, 37, 29]  
    Pass 4: [10, 13, 14, 29, 37]
    ```
    👉 Focus: Helps in debugging and understanding how the sort behaves at each step.


### Bubble Sort

1. Basic Bubble Sort (Ascending Order)

    **Problem:**
    Given an unsorted array of integers, sort it using the Bubble Sort algorithm.

    **Input:**
    ``` arr = [5, 3, 8, 4, 2] ```

    **Output:**
    ``` [2, 3, 4, 5, 8] ```

### Insertion Sort
-

### Merge Sort
-

### Quick Sort
-


## 5. Problems on Arrays /List

### Easy Level Problems
- Find the Largest Element in an Array.
- Find the Second Largest Element in an Array Without Sorting.
- Check if the array is sorted.
- Remove Duplicates from a Sorted Array [In-place].
 



    