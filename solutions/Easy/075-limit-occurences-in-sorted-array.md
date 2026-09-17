# 075. Limit Occurences in Sorted Array

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Arrays |
| **Solved on** | 2026-05-25 |
| **How I got there** | Minor Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:

        res = []
        prev = nums[0]
        res.append(prev)
        n= len(nums)
        count = 1

        for i in range( 1, n):
            curr = nums[i]
            if prev == curr and count <= k:
                count+=1
                if count > k:
                    pass
                else:
                    res.append(curr)
                
            elif curr != prev:
                prev = curr
                count = 1
                res.append(curr)

        return res
©leetcode
```
