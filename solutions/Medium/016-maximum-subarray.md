# 016. Maximum Subarray 

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | DP |
| **Solved on** | 2026-04-02 |
| **How I got there** | — |
| **Link** | [Problem link](https://leetcode.com/problems/maximum-subarray/description/) |

---

## Problem

Given an integer array `nums`, find the subarray with the largest sum, and return *its sum*.

**Example 1:**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

**Example 2:**

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

**Example 3:**

```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

**Constraints:**

* `1 <= nums.length <= 105`
* `-104 <= nums[i] <= 104`

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

## My Notes & Solution

Brute Force Solution:

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        maxsum = float('-inf')
        for i in range(n):
            for j in range(i,n):
                sum = 0
                for k in range(i,j+1):
                    sum+= nums[k]
                    maxsum = max(maxsum,sum)
        
        return maxsum

```

- This is essentially a n^3 solution which is absolutely bad.

DP implemented:

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum_arr = [0] * n
        sum_arr[0] = nums[0]
        if( len(nums) == 1):
            return nums[0]

        for i in range(1,n):
            currsum = nums[i]
            sum_arr[i] = max( currsum, (sum_arr[i-1] + currsum) )
        
        return max(sum_arr)
```
