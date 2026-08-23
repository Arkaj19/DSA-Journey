# 019. Longest Increasing Subsequence 

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | DP |
| **Solved on** | 2026-04-06 |
| **How I got there** | Saw Video Soution |
| **Link** | [Problem link](https://leetcode.com/problems/longest-increasing-subsequence/description/) |

---

## Problem

Given an integer array `nums`, return *the length of the longest **strictly increasing*** ***subsequence***.

**Example 1:**

```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

**Example 2:**

```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

**Example 3:**

```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

**Constraints:**

* `1 <= nums.length <= 2500`
* `-104 <= nums[i] <= 104`

**Follow up:** Can you come up with an algorithm that runs in `O(n log(n))` time complexity?

## My Notes & Solution

→ The length of the subsequence is equals to 2^n.
→ Here 2 is because each time we are either including or not including a subsequence.
→ the n represents the number of elements.

Hence the overall Time Complexity ⇒  O(2^n) 


- This leads to an exponential value which is not right.

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)

        dp = [1]*l
        lis = 1
        for i in range(1,l):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
            lis = max(lis,dp[i])
        
        return lis
```

- The +1 is due to the self counting being done here as well.
