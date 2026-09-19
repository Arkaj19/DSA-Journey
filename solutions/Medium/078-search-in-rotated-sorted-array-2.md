# 078. Search in Rotated Sorted Array 2

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Binary Search, Arrays |
| **Solved on** | 2026-06-05 |
| **How I got there** | Saw Video Soution |
| **Link** | [Problem link](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) |

---

## Problem

There is an integer array `nums` sorted in non-decreasing order (not necessarily with **distinct** values).

Before being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and become `[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` **after** the rotation and an integer `target`, return `true` *if* `target` *is in* `nums`*, or* `false` *if it is not in* `nums`*.*

You must decrease the overall operation steps as much as possible.

**Example 1:**

```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```

**Example 2:**

```
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

**Constraints:**

* `1 <= nums.length <= 5000`
* `-104 <= nums[i] <= 104`
* `nums` is guaranteed to be rotated at some pivot.
* `-104 <= target <= 104`

**Follow up:** This problem is similar to [Search in Rotated Sorted Array](/problems/search-in-rotated-sorted-array/description/), but `nums` may contain **duplicates**. Would this affect the runtime complexity? How and why?

## My Notes & Solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        ## Here it has duplicates   
        ## example: arr = [ 3,1,2,3,3,3,3 ]
        ## Here the problem is arr[low] == arr[mid] == arr[high] ( Whenever we get this condition we will shrink the search space)
        ## Then we need to shrink the search space i.e. low + 1 and high - 1

        low = 0
        high = len(nums) - 1
        
        while( low <= high):

            mid = (low + high) // 2
            if nums[mid] == target:
                return True

            ## Condition for shrinking our search space
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low+=1
                high-=1
                continue

            ## If all the low,mid and high are not equal then now we need to find the sorted half among them

            ## Considering left half to be sorted
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

- Here since there are duplicates a case can come when the low,mid and high values might be equal.

- In that kind of case we need to shrink the search window and then again try again because with the naked eye we can say that which side is sorted but the unqiue solution we can never infer that out.

- After that condition we will be doing the same step of finding the sorted half
