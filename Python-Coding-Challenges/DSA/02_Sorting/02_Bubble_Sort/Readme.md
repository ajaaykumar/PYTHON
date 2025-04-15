

## 🧠 **What is Bubble Sort?**

**Bubble Sort** is a simple sorting algorithm that works by **repeatedly swapping the adjacent elements** if they are in the wrong order. It’s called "bubble" sort because the biggest numbers **bubble up to the end** of the list with each pass.

---

## 👣 **How It Works – Step by Step**

Let’s sort this list in **ascending order**:  
`[5, 3, 8, 4, 2]`

We'll do **multiple passes** through the list. Each time, we compare two adjacent elements and **swap them if needed**.

---

### ✅ **Pass 1:**
Compare and swap if the left element is bigger than the right:

```
[5, 3, 8, 4, 2]   → Compare 5 and 3 → Swap → [3, 5, 8, 4, 2]
[3, 5, 8, 4, 2]   → Compare 5 and 8 → OK
[3, 5, 8, 4, 2]   → Compare 8 and 4 → Swap → [3, 5, 4, 8, 2]
[3, 5, 4, 8, 2]   → Compare 8 and 2 → Swap → [3, 5, 4, 2, 8]
```

👉 Biggest element `8` has **bubbled up** to the end.

---

### ✅ **Pass 2:**
```
[3, 5, 4, 2, 8]   → Compare 3 and 5 → OK
[3, 5, 4, 2, 8]   → Compare 5 and 4 → Swap → [3, 4, 5, 2, 8]
[3, 4, 5, 2, 8]   → Compare 5 and 2 → Swap → [3, 4, 2, 5, 8]
[3, 4, 2, 5, 8]   → Compare 5 and 8 → OK
```

👉 `5` is now in the correct position.

---

### ✅ **Pass 3:**
```
[3, 4, 2, 5, 8]   → Compare 3 and 4 → OK
[3, 4, 2, 5, 8]   → Compare 4 and 2 → Swap → [3, 2, 4, 5, 8]
[3, 2, 4, 5, 8]   → Compare 4 and 5 → OK
```

👉 `4` bubbles into place.

---

### ✅ **Pass 4:**
```
[3, 2, 4, 5, 8]   → Compare 3 and 2 → Swap → [2, 3, 4, 5, 8]
```

👉 Everything is now sorted! ✅

---

## 📊 Visualization

Here's a **simple diagram** showing the bubbling of the largest elements to the end:

```
Original:        [5, 3, 8, 4, 2]
After Pass 1:    [3, 5, 4, 2, 8]   → 8 is in place
After Pass 2:    [3, 4, 2, 5, 8]   → 5 is in place
After Pass 3:    [3, 2, 4, 5, 8]   → 4 is in place
After Pass 4:    [2, 3, 4, 5, 8]   → 3 and 2 are in place
```

---

## 🧮 Time Complexity
- Worst case: O(n²)  
- Best case (already sorted): O(n) (if you optimize with a `swapped` flag)  
- Space complexity: O(1) – it's an **in-place sort**

---

## ✅ Summary
- Compares **adjacent** elements
- **Swaps** if they're in the wrong order
- Repeats until no more swaps are needed
- Simple to understand, not efficient for large lists

---
