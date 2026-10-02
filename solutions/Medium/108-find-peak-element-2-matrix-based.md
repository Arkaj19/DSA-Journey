# 108. Find peak element 2 : Matrix based

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Binary Search, Arrays |
| **Solved on** | 2026-08-10 |
| **How I got there** | Needed Hint from ChatGpt |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        rows = len(mat)
        cols = len( mat[0])


        if cols == 1:
            
            max_r = 0
            max_val = -float('inf')
            for i in range( 0, rows):

                if mat[i][0] > max_val:
                    max_val = mat[i][0] 
                    max_r = i

            return [max_r,0]

                
        low = 0
        high = cols - 1

        
        while( low <= high ):

            mid = ( low + high)//2
            max_val = -float('inf')
            high_r = 0

            for i in range( 0, rows):

                if mat[i][mid] >= max_val:
                    max_val = mat[i][mid] 
                    high_r = i

            if mid > 0 and mid < cols - 1:
                if mat[high_r][mid] > mat[high_r][mid-1] and mat[high_r][mid + 1] < mat[high_r][mid]:
                    return [high_r,mid]
            
                elif  mat[high_r][mid] < mat[high_r][mid-1]:
                    high = mid - 1
                
                else:
                    low = mid + 1

            elif mid == cols - 1:

                if mat[high_r][mid] > mat[high_r][mid-1]:
                    return [high_r,mid]
                
                else:
                    high = mid - 1

            else:

                if mat[high_r][mid + 1] < mat[high_r][mid]:
                    return [high_r,mid]

                else:
                    low = mid + 1

        return [-1,-1]


```

#### Peak Element II (Matrix) — Your Revision Notes

- We perform binary search on columns, not on rows.

- For every middle column, find the maximum element in that column.

- Let its row index be high_r.

- Since it is the maximum in its column, we only need to compare it with its left and right neighbors.

- If:

---

#### Search Space

```plain text
low = 0
high = cols - 1
```

because we are binary searching on columns.

---

#### Direction Logic

If:

```plain text
left > current
```

then a peak must exist in the left half.

```plain text
high=mid-1
```

If:

```plain text
right > current
```

then a peak must exist in the right half.

```plain text
low=mid+1
```

---

#### Boundary Cases Handled

Only compare with right neighbor.

```plain text
current > right
```

⇒ Peak found.

---

Only compare with left neighbor.

```plain text
current > left
```

⇒ Peak found.

---

- Find the maximum element in the only column.

- Return its coordinates.

---

#### Complexity

Finding maximum in a column:

```plain text
O(rows)
```

Binary search on columns:

```plain text
O(log(cols))
```

Total:

```plain text
O(rows × log(cols))
```

---

#### Core Intuition

```plain text
Peak Element I:
Binary Search on indices.

Peak Element II:
Binary Search on columns.
Find column maximum first,
then decide left or right.
```

---

#### Interview One-Liner

> Pick the maximum element in the middle column. If it is larger than both left and right neighbors, it is a peak. Otherwise move towards the larger neighbor because a peak is guaranteed to exist in that direction.
