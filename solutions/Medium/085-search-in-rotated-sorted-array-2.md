# 085. Search in Rotated Sorted array 2

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Binary Search, Arrays |
| **Solved on** | 2026-06-26 |
| **How I got there** | Minor Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        low = 0
        high = len(nums) - 1

        while( low <= high):
            mid = (high + low) // 2
            if nums[mid] == target:
                return True

            if nums[mid] == nums[low] == nums[high]:
                low+=1
                high-=1
                continue

            ## LEFT HALF IS SORTED
            elif nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False 
```
