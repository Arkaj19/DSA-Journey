# 020. Partition Equal Subset Sum

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | DP |
| **Solved on** | 2026-04-06 |
| **How I got there** | Saw Video Soution |
| **Link** | [Problem link](https://leetcode.com/problems/partition-equal-subset-sum/description/) |

---

## Problem

Given an integer array `nums`, return `true` *if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or* `false` *otherwise*.

**Example 1:**

```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

**Example 2:**

```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

**Constraints:**

* `1 <= nums.length <= 200`
* `1 <= nums[i] <= 100`

## My Notes & Solution

- Basic Recursive Approach:

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = 0
        sum = 0
        self.dp = {}
        for idx,num in enumerate(nums):
            sum += num
        
        if sum % 2 != 0:
            return False
        
        target = sum // 2

        return self.partition(0,target,nums)

    def partition( self, i,target,nums):
        if target == 0:
            return True
        
        if i == len(nums):
            return False
        
        if nums[i] in self.dp:
            return self.dp[nums[i]]
        
        if target < 0:
            return False
        

        not_take = self.partition(i+1, target, nums)

        take = False
        if nums[i] <= target:
            take = self.partition(i+1, target - nums[i], nums)
        
        self.dp[nums[i]] = take or not_take
        return self.dp[nums[i]]
```

- DP Memoization result

```javascript
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = 0
        sum = 0
        self.dp = {}
        for idx,num in enumerate(nums):
            sum += num
        
        if sum % 2 != 0:
            return False
        
        target = sum // 2

        return self.partition(0,target,nums)

    def partition( self, i,target,nums):
        if target == 0:
            return True

        if i == len(nums):
            return False
        
        if target < 0:
            return False
        
        if (i,target) in self.dp:
            return self.dp[(i,target)]
        
        not_take = self.partition(i+1, target, nums)

        take = False
        if nums[i] <= target:
            take = self.partition(i+1, target - nums[i], nums)
        
        self.dp[(i,target)] = take or not_take
        return self.dp[(i,target)]
```

→ Here we are using a tuple of (i, target ) as the key for the dp.

Base Cases:

- The First case is when the target == 0 then we return True.

- We need a counter that if i == len(nums) then we need to return False because else our i will keep on increasing exponentially.

- We need to also maintain the target < 0 because if the value because less at any moment then there’s no use traversing further in that path.

Here we implement the leave or take policy.

→ Each time we dont take which is for sure.
→ We only take in cases where the nums[i] is less than target as then we will be able to say that adding the nums[i] to the target will be valid .

because if a value is 12 and the target is 9 ther’s no use.
