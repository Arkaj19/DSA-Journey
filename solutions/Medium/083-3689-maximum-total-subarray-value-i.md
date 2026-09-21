# 083. 3689. Maximum Total Subarray Value I

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Arrays |
| **Solved on** | 2026-06-09 |
| **How I got there** | Minor Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

- This is a really absurd question.

- But since it was allowed that the same interval can be taken k times hence I just took out the max and min value out of them and then multiplied it with k.

Hence we got the result.

```python
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        
        max_val = max(nums)
        min_val = min(nums)

        res = k * ( max_val - min_val)

        return res
```
