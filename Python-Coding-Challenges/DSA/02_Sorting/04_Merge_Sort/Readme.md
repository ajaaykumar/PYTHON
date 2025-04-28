
## 🧠 What is Merge Sort?

**Merge Sort** is a **Divide and Conquer** algorithm.

> 🪓 **It breaks down** the list into smaller parts (until each part has 1 element),  
> 🧩 then **merges** them back together in **sorted order**.

Think of it like tearing a deck of cards into single cards, then **merging** them back **in order**.

---

## 🔧 How Does Merge Sort Work?

Let's take this array as an example:  
```
[6, 3, 8, 5]
```

---

### ✅ Step 1: **Divide the array**
Keep splitting the array into halves until you get arrays of size 1 (because a single number is already sorted):

```
[6, 3, 8, 5]
↓
[6, 3]     [8, 5]
↓
[6] [3]    [8] [5]
```

---

### ✅ Step 2: **Merge the smaller sorted arrays**

Start combining arrays **in sorted order**:

- Merge `[6]` and `[3]` → `[3, 6]`  
- Merge `[8]` and `[5]` → `[5, 8]`

```
[6] + [3] → [3, 6]  
[8] + [5] → [5, 8]
```

---

### ✅ Step 3: **Merge the merged arrays**

Now merge `[3, 6]` and `[5, 8]` into one sorted array:

```
[3, 6] + [5, 8] → [3, 5, 6, 8]
```

🎉 Done!

---

## 📊 Diagram: Merge Sort in Action

```
Original:         [6, 3, 8, 5]

Divide:           [6, 3]      [8, 5]
                 /    \      /    \
                [6]   [3]   [8]   [5]

Merge:            ↓      ↓     ↓     ↓
                [3, 6]        [5, 8]

Final Merge:     [3, 5, 6, 8]
```

---

## 🧮 Time & Space Complexity

| Case         | Time     | Space     |
|--------------|----------|-----------|
| Best Case    | O(n log n) | O(n)     |
| Worst Case   | O(n log n) | O(n)     |
| Stable Sort? | ✅ Yes    |

✅ Merge Sort is **efficient and consistent**, especially for large datasets.

---

## 🎯 Summary

| Feature         | Explanation                      |
|------------------|----------------------------------|
| Type             | Divide and Conquer               |
| Good for         | Large datasets                   |
| Not good for     | Tiny datasets (Insertion sort is better) |
| In-place?        | ❌ Needs extra memory (O(n))     |
| Stable?          | ✅ Keeps equal elements in order |



