# 069. Rotate a Matrix by 180 Counterclockwise

| | |
|---|---|
| **Platform** | GFG |
| **Difficulty** | Medium |
| **Topics** | Matrix |
| **Solved on** | 2026-05-05 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://www.geeksforgeeks.org/problems/c-matrix-rotation-by-180-degree0745/1) |

---

## Problem

_Couldn't auto-fetch the statement (paid-only question, or the source page changed). See the [original link](https://www.geeksforgeeks.org/problems/c-matrix-rotation-by-180-degree0745/1)._

## My Notes & Solution

```python
class Solution:
	def rotateMatrix(self, mat):
		# Code here
		
		# Transposing from left to right diagonal
		
		rows = len(mat)
		cols = len(mat[0])
		
		for i in range(rows):
		    for j in range(cols // 2):
		        
		        mat[i][j], mat[i][cols-1-j] =  mat[i][cols - 1-j], mat[i][j]
		 
# 		print(mat)
		
		for j in range(cols):
		    for i in range( rows // 2):
		        
		        mat[rows-1-i][j],mat[i][j] = mat[i][j],mat[rows-1-i][j]
```

- Here we are basically first reversing the row and then reversing the column,

- That’s all we are doing here.

- This is done when we need to rotate the matrix by 180 degrees
