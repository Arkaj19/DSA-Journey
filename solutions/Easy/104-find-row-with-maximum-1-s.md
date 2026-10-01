# 104. Find row with maximum 1's

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Binary Search, Arrays |
| **Solved on** | 2026-08-06 |
| **How I got there** | Minor Thinking required, Saw Video Soution |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

Naive Solution

```python
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        m = len(mat) ## rows
        n = len( mat[0]) ## columns

        row_sum = []

        for i in range( m):
            temp = 0
            for j in range( n):
                temp+= mat[i][j]
            row_sum.append(temp)

        print(row_sum)

        max_sum = max(row_sum)

        for idx,s in enumerate(row_sum):

            if s == max_sum:
                return [idx,s]

        return -1
```

Binary Search Solution

```python
class Solution:
    def rowWithMax1s(self, arr):
        # code here
        m = len(arr) ## rows
        n = len( arr[0]) ## columns

        row_sum = []

        for i in range( m):
            temp = float('inf')
            
            low = 0
            high = n-1

            while ( low <= high):

                mid = (low + high) // 2
                if arr[i][mid] == 1:

                    temp = min(temp,mid)
                    high = mid - 1
                    
                else:
                    low = mid + 1
            
            if temp == float('inf'):
                row_sum.append(0)
            else:
                row_sum.append( n - temp)

        # print(row_sum)

        max_sum = max(row_sum)
        if max_sum == 0:
            return -1

        for idx, s in enumerate(row_sum):

            if s == max_sum:
                return idx

        return -1
```

- The first for loop is indispensable as it is used to iterate over each of the rows.

- The next while loop is essential for the binary search algorithm.
