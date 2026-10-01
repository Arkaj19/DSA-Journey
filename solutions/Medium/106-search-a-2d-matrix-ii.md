# 106. Search a 2d matrix II

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Binary Search, Arrays |
| **Solved on** | 2026-08-07 |
| **How I got there** | Minor Thinking required, Needed Hint from ChatGpt, Saw Video Soution |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

Search a 2D Matrix II (LeetCode 240)

- Matrix is not globally sorted, so the 1D flattening trick from Search Matrix I cannot be used.

- Rows are sorted left → right.

- Columns are sorted top → bottom.

#### Key Observation

Start from the top-right corner.

```plain text
If current > target → move left
If current < target → move down
If current == target → found
```

#### Why?

- Moving left gives smaller values.

- Moving down gives larger values.

- At every step, one entire row or column is eliminated.

#### Algorithm

```plain text
r = 0
c = n - 1

while r < rows and c >= 0:
    if matrix[r][c] == target:
        return True
    elif matrix[r][c] > target:
        c -= 1
    else:
        r += 1

return False
```

#### Complexity

- Time: O(m + n)

- Space: O(1)

#### Pattern Recognition

- Search Matrix I (74) → Globally sorted → Binary Search on answer space → O(log(m*n))

- Search Matrix II (240) → Row-wise + Column-wise sorted → Staircase Search → O(m+n)

- This is the most optimal approach which just uses the concept of pointers and the proper elimination of rows and columns.

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix)
        col = len( matrix[0])

        c = col - 1
        r = 0

        while ( c >= 0 and r < row):

            if matrix[r][c] == target:
                return True

            elif matrix[r][c] > target:
                c-=1
            
            elif matrix[r][c] < target:
                r+=1

        return False
```

Binary Search Approach:

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len( matrix[0])

        for i in range( m):

            low = 0
            high = n - 1

            if matrix[i][0] <= target and matrix[i][n-1] >= target:

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
