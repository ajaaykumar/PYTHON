---
## 🧠 What is **Selection Sort**?

**Selection Sort** is a simple sorting algorithm that works by:

> 🔍 **Finding the smallest (or largest) element from the unsorted part and putting it at the beginning.**

It divides the array into two parts:
- ✅ **Sorted part** (starts empty)
- ❌ **Unsorted part**

---

## 🎯 How Selection Sort Works (Step-by-Step)

Let’s sort this array in **ascending order**:  
```
[5, 3, 8, 4, 2]
```

---

### ✅ Step 1:
Look at the **entire array** to find the **smallest number**.

Smallest = `2`

👉 Swap it with the first number (`5`)

```
Before: [5, 3, 8, 4, 2]  
After:  [2, 3, 8, 4, 5]
         ↑
     Sorted part
```

---

### ✅ Step 2:
Now, look at the remaining unsorted part: `[3, 8, 4, 5]`  
Smallest = `3`

Already at the correct position — no swap needed.

```
[2, 3, 8, 4, 5]
     ↑↑
   Sorted part
```

---

### ✅ Step 3:
Look at `[8, 4, 5]`  
Smallest = `4` → Swap with `8`

```
Before: [2, 3, 8, 4, 5]  
After:  [2, 3, 4, 8, 5]
         ↑↑↑
     Sorted part
```

---

### ✅ Step 4:
Look at `[8, 5]`  
Smallest = `5` → Swap with `8`

```
Before: [2, 3, 4, 8, 5]  
After:  [2, 3, 4, 5, 8]
         ↑↑↑↑
     Sorted part
```

---

🎉 Now the array is **fully sorted**!

---

## 📊 Visualization Diagram

Here’s how the selection sort "selects" the smallest each time:

```
Pass 1: [5, 3, 8, 4, 2] → [2, 3, 8, 4, 5]
Pass 2: [2, 3, 8, 4, 5] → [2, 3, 8, 4, 5]
Pass 3: [2, 3, 8, 4, 5] → [2, 3, 4, 8, 5]
Pass 4: [2, 3, 4, 8, 5] → [2, 3, 4, 5, 8]
```

✅ In each pass, the smallest element is placed where it belongs.

---

## 📉 Time Complexity

| Case        | Time     |
|-------------|----------|
| Best Case   | O(n²)    |
| Worst Case  | O(n²)    |
| Space       | O(1)     |

Selection Sort is **not efficient** for large data, but it's very good for **learning sorting basics**.

---