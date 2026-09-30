# 103. kth element of 2 sorted arrays

| | |
|---|---|
| **Platform** | GFG |
| **Difficulty** | Medium |
| **Topics** | Binary Search, Arrays |
| **Solved on** | 2026-08-05 |
| **How I got there** | Major Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
Better Approach

class Solution:
    def kthElement(self, a, b, k):
        # code here
        
        c = []
        
        i = 0
        j = 0
        n1 = len(a)
        n2 = len(b)
        
        while( i < n1 and j < n2):
            
            if a[i] <= b[j]:
                c.append(a[i])
                i+=1
                
            else:
                c.append(b[j])
                j+=1
                
        while( i < n1):
            c.append(a[i])
            i+=1
            
        while( j < n2):
            c.append(b[j])
            j+=1
                
        if len(c) < k:
            return -1
            
        if len(c) == k:
            return c[len(c) - 1]
        for i in range( len(c)):
            
            if i+1 == k:
                return c[i]
        
        return -1
                
        
                
```
