## 🧠 What is Quick Sort?

**Quick Sort** is a **Divide and Conquer** algorithm — just like Merge Sort — but it works a bit differently.

> It picks a number (called the **pivot**) and then:
> - Puts all **smaller numbers to the left** of it
> - Puts all **larger numbers to the right**
> - Then **repeats** the process for the left and right sides

---

## 🧩 Real-Life Analogy

Imagine you're organizing pizza slices 🍕 of different sizes:
- You pick one slice as your **pivot slice**
- Put all **smaller slices** to the **left**
- Put all **bigger slices** to the **right**
- Repeat for the left and right piles until all slices are sorted

---

## 🔄 Step-by-Step Example

Let’s sort this array:
```
[6, 3, 8, 5, 2]
```

### ✅ Step 1: Choose a Pivot

Let’s say we pick the **last element** as the pivot → `2`

```
[6, 3, 8, 5, 2]
             ↑
           Pivot
```

We rearrange so that numbers smaller than `2` go to the left, and larger go to the right.

**All numbers are larger**, so `2` swaps with `6` and goes to the front:
```
[2, 3, 8, 5, 6]
 ↑
Pivot is now in the right place!
```

---

### ✅ Step 2: Apply Quick Sort to the Left and Right

Left of `2` → no elements → nothing to sort

Right of `2` → `[3, 8, 5, 6]`

Choose `6` as pivot

- `3 < 6`, `8 > 6`, `5 < 6`

Rearranged:
```
[3, 5, 6, 8]
           ↑
        Pivot
```

Now apply again to `[3, 5]` and `[8]`

Eventually you get:
```
[2, 3, 5, 6, 8]
```

🎉 Done!

---

## 📊 Visual Diagram

``` YAML
Original:        [6, 3, 8, 5, 2]
Choose Pivot:                     2
Partitioned:      [2, 3, 8, 5, 6] ← Pivot is placed at its correct position

Subarrays:             [3, 8, 5, 6]
Choose Pivot:                             6
Partitioned:            [3, 5, 6, 8]

Keep splitting until everything is sorted
Final Sorted:   [2, 3, 5, 6, 8]
```

---

## ⏱️ Time and Space Complexity

| Case         | Time     | Space |
|--------------|----------|--------|
| Best Case    | O(n log n) | O(log n) (due to recursion)
| Average Case | O(n log n) | O(log n)
| Worst Case   | O(n²)     | O(log n) (when pivot is always smallest or largest)

---

## 🧠 Key Points Recap

| Concept       | Description                                 |
|---------------|---------------------------------------------|
| Pivot         | Element used to split the array             |
| Partitioning  | Placing smaller left and larger right       |
| Recursive     | Quick Sort is applied to each half          |
| In-Place      | ✅ It doesn’t need extra arrays (unlike merge sort) |
