# 067. Rotate Image

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Matrix |
| **Solved on** | 2026-05-04 |
| **How I got there** | Needed Hint from ChatGpt |
| **Link** | [Problem link](https://leetcode.com/problems/rotate-image/description/?envType=daily-question&envId=2026-05-04) |

---

## Problem

You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm), which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)

```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

**Constraints:**

* `n == matrix.length == matrix[i].length`
* `1 <= n <= 20`
* `-1000 <= matrix[i][j] <= 1000`

## My Notes & Solution

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len( matrix[0])
        
        ## Here we have performed the transposition

        for i in range( 0, rows):
            for j in range( i,cols):

                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        
        ## Here we are reversing each of the rows
        
        for i in range( 0, rows):
            for j in range( 0,cols//2):

                matrix[i][j],matrix[i][cols - 1 - j] = matrix[i][cols -1 - j],matrix[i][j]
            
        # print(matrix)
```

- Here we need to first transpose the matrix that is the row ↔ column .

- Then we will be reversing each row of the matrix.

- Hence this is the best in-place solution available for the rotation of the matrix.

```python
90 = transpose + reverse row
180 = reverse row + reverse column
270 = transpose + reverse col
```
