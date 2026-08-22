# 017. Maximum Product Subarray

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | DP |
| **Solved on** | 2026-04-03 |
| **How I got there** | — |
| **Link** | [Problem link](https://leetcode.com/problems/maximum-product-subarray/description/) |

---

## Problem

Given an integer array `nums`, find a subarray that has the largest product, and return *the product*.

The test cases are generated so that the answer will fit in a **32-bit** integer.

**Note** that the product of an array with a single element is the value of that element.

**Example 1:**

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

**Example 2:**

```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

**Constraints:**

* `1 <= nums.length <= 2 * 104`
* `-10 <= nums[i] <= 10`
* The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit** integer.

## My Notes & Solution

- If my nums array has even number of negative values then the overall product will become +ve.

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        maxprod = [1] * l
        minprod = [1] * l
        maxprod[0] = nums[0]
        minprod[0] = nums[0]
        curr = nums[0]
        for i in range(1,l):
            curr = nums[i]
            maxprod[i] = max( curr, maxprod[i-1] * curr, minprod[i-1] * curr)
            minprod[i] = min( curr, maxprod[i-1]*curr,minprod[i-1] * curr)

        return max(maxprod)
```

- Here we need to maintain 2 arrays which is the max and the min array. THis is because sometimes we might momentarily feel that -40 is less than 10 but later if another -2 comes then the -40 will become +80 and the 10 will become -20. 

- Hence we need to keep that in consideration.

- At each time we need to consider which to be considered as the max and the min.

The candidates are : 

1. Current element at that moment → nums[i]
2. Current element * Previous element in the max array → nums[i] * maxprod[i-1]
3. Current element * Previous element in the min array → nums[i] * minprod[i-1]
