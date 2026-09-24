# 090. Find nth root of an integer

| | |
|---|---|
| **Platform** | GFG |
| **Difficulty** | Medium |
| **Topics** | Binary Search |
| **Solved on** | 2026-07-07 |
| **How I got there** | Saw Video Soution |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

Naive Approach

- The naive approach would be to just run a for loop to run from 0 to the number itself.

- Check the power(i,n) and check if its equal to the target value.

- If at any instant it exceeds then we break and return -1 as the answer.

```python
class Solution:
    def nthRoot(self, n, m):
       # code here
       
       for i in range( m+1):
           
           check = pow(i,n)
           
           if check == m:
               return i
               
           elif check > m:
                break
            
        
       return -1
          

```

Optimized Binary Search Approach

```python
class Solution:
    def nthRoot(self, n, m):
       # code here
       
        if m == 0:
           return 0
           
        low = 1
        high = m
        
        while( low <= high ):
            
            mid = (low + high) // 2
            if pow(mid,n) == m:
                return mid
            
            elif pow(mid,n) > m:
                high = mid - 1
                
            elif pow(mid,n) < m:
                low = mid + 1
        
        return -1
```
