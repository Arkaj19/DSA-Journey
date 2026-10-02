# 109. Matrix median 

| | |
|---|---|
| **Platform** | GFG |
| **Difficulty** | Medium |
| **Topics** | Binary Search, Arrays |
| **Solved on** | 2026-08-10 |
| **How I got there** | Saw Video Soution |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

Naive Approach

```python
class Solution:
    def median(self, mat):
    	# code here 
    	
        rows = len(mat)
        cols = len(mat[0])
        
        r = 0
        col = 0
        
        arr= []
        
        for i in range( rows):
            
            for j in range( cols):
                
                arr.append(mat[i][j])
                
        
        arr.sort()
        
        total = rows * cols
        
        mid = total // 2
        
        return arr[mid]
            
```

- Take all the values in an array sort it and then return the median value.

Optimal Approach
