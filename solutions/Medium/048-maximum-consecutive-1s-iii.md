# 048. Maximum Consecutive 1s III 

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Sliding Window, Two Pointers |
| **Solved on** | 2026-04-22 |
| **How I got there** | Could solve it instantly |
| **Link** | [Problem link](https://leetcode.com/problems/max-consecutive-ones-iii/) |

---

## Problem

Given a binary array `nums` and an integer `k`, return *the maximum number of consecutive* `1`*'s in the array if you can flip at most* `k` `0`'s.

**Example 1:**

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

**Example 2:**

```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

**Constraints:**

* `1 <= nums.length <= 105`
* `nums[i]` is either 0 or 1.
* `0 <= k <= nums.length`

## My Notes & Solution

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        left = 0
        right = 0
        # curr_window = 0
        max_window = 0
        zeroes = 0

        while right < n:

            num = nums[right]
            if num == 0:
                zeroes+=1
            
            while( zeroes > k):
                
                if nums[left] == 0:
                    zeroes-=1
                    left+=1
                else:
                    left+=1
            
            max_window = max(right - left + 1, max_window)
            right+=1
        
        return max_window
```

- Here basically what we are doing is that we are increasing the right pointer always but we are also keeping in mind that if a zero is encountered then we are increasing zeroes by 1

- There is a while loop which controls whether to decrease the zeroes and increase the left counter. 

- The zeroes decreases only when the left pointer is on a zero which is to be omitted.

- This question is not about flipping but about whether there are 2 or less zeroes in our window or not.
