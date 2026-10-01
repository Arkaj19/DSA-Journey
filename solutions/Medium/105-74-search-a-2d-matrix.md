# 105. 74. Search a 2D Matrix

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Binary Search, Arrays |
| **Solved on** | 2026-08-06 |
| **How I got there** | Saw Video Soution, Major Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len( matrix[0])

        for i in range( m):

            low = 0
            high = n - 1

            if matrix[i][0] < target and matrix[i][n-1] > target:

                while( low <= high ):

                    mid = (low + high)// 2
                    if matrix[i][mid] == target:
                        return True

                    elif matrix[i][mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1

            else:
                continue

        return False
```

Binary Search

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len( matrix[0])

        low = 0
        high = ( n * m) - 1

        while( low <= high ):

            mid = (low + high)// 2
            row = mid // n
            col = mid % n 
            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
```
