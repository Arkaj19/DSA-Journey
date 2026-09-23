# 087. Find Minimum in Rotated Sorted Array

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Binary Search |
| **Solved on** | 2026-06-29 |
| **How I got there** | Saw Video Soution |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        ans = float('inf')
        low = 0
        high = len(nums) - 1

        while( low <= high):
            mid = ( low + high ) // 2

            if nums[low] <= nums[mid]:
                ans = min( ans, nums[low])
                low = mid + 1

            else:
                ans = min( ans, nums[mid])
                high = mid - 1
            
        
        return ans
```

- Here it basically means that we are trying to first find which side is sorted and then as we find the sorted half then we are trying to just check the first character of that half as is it less than our result then it will be our new min.

- This is because the first digit of a sorted half is always going to be the smallest and after accessing that value then we practically have no need for the rest of that portion because we have already taken the smallest element out of it.
