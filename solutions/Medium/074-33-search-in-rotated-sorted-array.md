# 074. 33. Search in Rotated Sorted Array

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Arrays, Binary Search |
| **Solved on** | 2026-05-15 |
| **How I got there** | Saw Video Soution |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        ## Brute Force ( Linear Search )
        # for idx,num in enumerate(nums):
        #     if num == target:
        #         return idx

        # return -1

## ===========================================================================================  ##

        ## Optimized Approach i.e. ---> Binary Search <---
        ## Because the array is sorted we can eliminate portions and go for a Binary Search approach

        # 1. IDENTIFY THE SORTED HALF : left or right

        low = 0
        high = len(nums) - 1

        while( low <= high):

            mid = ( low + high ) // 2
            if nums[mid] == target:
                return mid

            ## Now we need to find the sorted side

            ## Left side sorted
            if nums[low] <= nums[mid]:

                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            ## Right side sorted
            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1
```

- Here we need to apply binary search here such that to eliminate one half of the array at each time.

- Every time first we need to check which part of the array is sorted and which is not sorted.

- Then we check if the number belongs in that sorted portion if not then we are forced to take the unsorted portion.

-
