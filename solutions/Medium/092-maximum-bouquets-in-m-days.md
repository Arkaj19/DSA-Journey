# 092. maximum bouquets in M days

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Binary Search |
| **Solved on** | 2026-07-18 |
| **How I got there** | Saw Video Soution |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

- The first thing to do in these kind of questions is to find the range of the solution first. 

- That is the biggest trick like here we know that if m*k < n then we are never getting the solution.

- Because we dont have that many elements to get adjacent values.

```python
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m*k > len(bloomDay):
            return -1
        
        ans = -1
         
        low = min(bloomDay)
        high = max(bloomDay)

        while( low <= high ):
            mid = (low + high) // 2

            if self.possible(bloomDay, mid, m , k):
                ans = mid
                high = mid - 1
            
            else:
                low = mid + 1
        
        return ans

    def possible(self, bloomDay, mid, m , k):

        cons_count = 0
        bouquets = 0
        
        for bloom in bloomDay:

            if bloom <= mid:
                cons_count+=1
                if cons_count == k:
                    bouquets+=1
                    cons_count = 0

            else:
                cons_count = 0

        return bouquets >= m
```
