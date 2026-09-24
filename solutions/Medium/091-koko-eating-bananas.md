# 091. koko eating bananas

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Binary Search |
| **Solved on** | 2026-07-10 |
| **How I got there** | Saw Video Soution |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = max(piles)
        ans = float('inf')

        while( low <= high):

            mid = (low + high) // 2
            hrs = self.cal(piles,mid)
            if  hrs <= h:
                ans = min(ans,mid)
                high = mid - 1

            elif hrs > h:
                low = mid + 1

        return ans

    def cal( self, piles, mid):

        total_hrs = 0

        for i in range(len(piles)):
            total_hrs+= math.ceil(piles[i] / mid)
        
        return total_hrs
```

- Here the thing is that We know that the maximum bananas that koko can eat is the max value of piles in an hour aand the lowest is 1.

- Hence we run a binary search through  that.

- Then everytime we also calculate the total hours value and then return it.

- Now if the total hours is less than h then we try to see if it is the min answer and we reduce the high because there is no use going high above and we need to get the least value.

- if the value is higher than h then then we need to increase the no. of bananas per hour for koko hence we increase the value of low to mid + 1.

- This is how we do the Binary search on answers.
