
# 📘 Array Creation in Python 

Create arrays in Python using **List**, **array module**, and **NumPy**.

---

## ✅ 1. Using Python List (Dynamic Array)
Python lists behave like dynamic arrays and are most commonly used in DSA.

### ➤ Create a list
```python
arr = [10, 20, 30]
```

### ➤ Empty list
```python
arr = []
```

### ➤ Using list()
```python
arr = list([1, 2, 3])
```

### ➤ Using range()
```python
arr = list(range(5))   # [0, 1, 2, 3, 4]
```

### ➤ Repeated values
```python
arr = [0] * 5          # [0, 0, 0, 0, 0]
```

---

## ✅ 2. Using `array` Module (True Homogeneous Arrays)
The `array` module stores elements of a single data type.

### ➤ Syntax
```python
from array import array
arr = array('i', [1, 2, 3, 4])   # 'i' = integer
```

### ➤ Empty array
```python
arr = array('i', [])
```

### ➤ Common Typecodes
| Code | Meaning |
|------|---------|
| `i`  | integer |
| `f`  | float   |
| `d`  | double  |

---

## ✅ 3. Using NumPy Arrays (2D, 3D, ML Arrays)
NumPy is used for numerical, scientific, and multi-dimensional arrays.

### ➤ Import
```python
import numpy as np
```

### ➤ Basic array
```python
arr = np.array([1, 2, 3])
```

### ➤ Array with datatype
```python
arr = np.array([1, 2, 3], dtype='int32')
```

### ➤ 2D array
```python
matrix = np.array([[1, 2], [3, 4]])
```

### ➤ Zeros / Ones
```python
np.zeros(5)
np.ones((2, 3))
```

### ➤ Range
```python
np.arange(1, 10, 2)
```

---

## ⭐ Key Takeaways
- Python **lists** = dynamic arrays (flexible, used in interviews).
- `array` module = **homogeneous arrays** (need typecode).
- NumPy arrays = best for **matrix / 2D / 3D operations**.
- Set data type using `dtype=` in NumPy.
- Always import NumPy like:
```python
import numpy as np
```
- Never call the module:
```python
❌ np([1,2,3])
✔️ np.array([1,2,3])
```

---

## 🚀 Quick Practice
1. Create a list `[1, 2, 3]`.  
2. Create an integer array using `array('i', [...])`.  
3. Create a NumPy float32 array.  
4. Create a 2D NumPy array `[[1, 2], [3, 4]]`.  
5. Create an array of 5 zeros using NumPy.
