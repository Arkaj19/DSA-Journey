# 041. Search Insert Position

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Binary Search |
| **Solved on** | 2026-04-21 |
| **How I got there** | Could solve it instantly |
| **Link** | [Problem link](https://leetcode.com/problems/search-insert-position/) |

---

## Problem

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Example 2:**

```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

**Example 3:**

```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

**Constraints:**

* `1 <= nums.length <= 104`
* `-104 <= nums[i] <= 104`
* `nums` contains **distinct** values sorted in **ascending** order.
* `-104 <= target <= 104`

## My Notes & Solution

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        start = 0
        end = n - 1
        mid = 0

        return self.find_num(nums,start,end,mid,target)
    
    def find_num(self,nums,start,end,mid,target):

        while( start <= end):

            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                return self.find_num( nums,mid + 1, end, mid,target)
            
            elif nums[mid] > target:
                # end = mid - 1
                return self.find_num( nums,start, mid - 1, mid,target)

        return start
```

- This is a basic problem of Binary Search

- If the element is not found then it is to be placed in the last left position that we checked.
