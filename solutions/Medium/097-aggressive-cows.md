# 097. Aggressive Cows

| | |
|---|---|
| **Platform** | GFG |
| **Difficulty** | Medium |
| **Topics** | Binary Search |
| **Solved on** | 2026-07-30 |
| **How I got there** | Saw Video Soution |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

- This is going to be a bit different from the other concepts of the Binary Search on Answers problem as it will have the answers coming as max (min) or min (max) .

- The minimum will always come between the consecutive stalls.

- 

```python
class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        
        arr.sort()
        
        low = 1
        high = max(arr)
        ans = -float('inf')
        
        while( low <= high):
            
            mid = (low + high) // 2
            
            if self.check(arr, mid, k):
                # print(f"True came for mid value : {mid}")
                ans = max(ans, mid)
                low = mid + 1
            
            else:
                # print(f"False came for mid value : {mid}")
                high = mid - 1
        
        return ans
        
    
    def check( self, arr, mid, k):
        
        count = 1
        min_val = arr[0]
        
        for i in range(1,len(arr)):
            
            if arr[i] - min_val >= mid:
                count+=1
                min_val = arr[i]
            else:
                continue
            
            
        if count >= k:
            return True
        else:
            return False
            
             
```
