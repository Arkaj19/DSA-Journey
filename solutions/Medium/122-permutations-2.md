# 122. Permutations 2

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Recursion |
| **Solved on** | 2026-08-27 |
| **How I got there** | Major Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def find( idx, curr, pos_arr):

            if len(curr) == len(nums) and curr not in res:
                res.append(curr.copy())
                return
            
            for i in range( 0, len(nums)):

                if i not in pos_arr:
                    pos_arr.add(i)
                    curr.append(nums[i])
                    find( i+1, curr, pos_arr)
                
                else:
                    continue
                
                curr.pop()
                pos_arr.remove(i)

        find( 0, [], set())
        return res
```

-
