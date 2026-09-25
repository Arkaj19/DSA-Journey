# 094. 1283. Find the Smallest Divisor Given a Threshold

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Binary Search |
| **Solved on** | 2026-07-28 |
| **How I got there** | Major Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        low = 1
        high = max(nums)
        ans = float('inf')
        q = float('inf')

        while( low <= high):

            mid = (low + high) // 2
            res = self.divide(nums, mid)
            if res <= threshold:
                q = min(q, mid)
                high = mid - 1
            
            else:
                low = mid + 1
        
        return q
    
    def divide( self, nums, mid):

        sum = 0

        for n in nums:
            sum+= math.ceil(n / mid)

        return sum
```

- Here the thing is that once we get a threshold we will need to go on the left side and not the right side because although we know that going on the left might increase the threshold score but our aim is to reach the lowest divisor which still remains in the left side.
