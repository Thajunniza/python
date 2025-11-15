# ✨ What is a List?

A **list** in Python is a dynamic, ordered collection that can store
multiple values of different data types.

``` python
my_list = [10, "apple", 3.14, True]
```

## 🧠 Key Properties

  Property            Meaning
  ------------------- -------------------------------------
  **Ordered**         Elements maintain insertion order
  **Mutable**         You can change items after creation
  **Dynamic size**    Grows/shrinks automatically
  **Heterogeneous**   Can store mixed data types

## 🏗️ Common List Operations

### Create

``` python
nums = [1, 2, 3]
empty = []
```

### Access

``` python
nums[0]      # 1
nums[-1]     # 3
```

### Modify

``` python
nums[1] = 10
```

### Insert / Append

``` python
nums.append(4)
nums.insert(1, 99)
```

### Delete

``` python
nums.pop()
nums.pop(2)
del nums[1]
nums.remove(10)
```

## 🔁 Looping

``` python
for item in nums:
    print(item)
```

## 🧮 Common List Methods

  Method         Description
  -------------- ------------------
  append()       Add at end
  insert(i, x)   Add at index
  pop(i)         Remove by index
  remove(x)      Remove by value
  sort()         Sort ascending
  reverse()      Reverse list
  extend()       Add another list

## ⚙️ Time & Space Complexity

### Indexing: **O(1)**

### Insert/Delete:

-   End → O(1)
-   Middle → O(n)

### Search: **O(n)**

### Space: **O(n)**

## ⭐ Quick Decision Table

  Scenario                Use List?        Reason
  ----------------------- ---------------- ----------------
  Fast indexing           ✔ Yes            O(1) access
  Frequent append         ✔ Yes            Amortized O(1)
  Random access           ✔ Yes            Efficient
  Fast middle insertion   ❌ No            O(n) shifting
  Queue operations        ❌ Use deque     O(1) popleft
  Numeric operations      ❌ NumPy array   Optimized
  Mixed data storage      ✔ Yes            Flexible

## 🧠 When to Use Lists

✔ Indexing needed\
✔ Order matters\
✔ Moderate size changes

## 🚫 When to Avoid Lists

❌ Need constant-time insert/delete\
❌ Heavy numerical computation\
❌ Queue-heavy workflows
