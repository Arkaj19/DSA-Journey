# 010. House Robber

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | DP |
| **Solved on** | 2026-03-22 |
| **How I got there** | Saw Video Soution |
| **Link** | [Problem link](https://leetcode.com/problems/house-robber/) |

---

## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

**Example 2:**

```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

**Constraints:**

* `1 <= nums.length <= 100`
* `0 <= nums[i] <= 400`

## My Notes & Solution

→ The first thing is that its not that we need to compulsarily rob every next house and it can be that we can rob one house and then again rob the house aafter two houses.

→ The only constraint is that at least there should be a gap of one house between the robbing.
→ This question can also be considered an alternative of the Fibonnaci Series.
→ Here, also the thing is that we need to take the solution of (i-1)th solution and (i - 2)th solution.


### Tabulation ( Iterative ) 

```java
class Solution {
    public int rob(int[] nums) {

        //Edge Cases
        if( nums.length == 1) // If the array has 1 element
        return nums[0];
        
        if( nums.length == 2) // If the array has 2 elements
        {
            return Math.max( nums[0], nums[1]);
        }

        int n = nums.length;
        int []arr = new int[n];
        arr[0] = nums[0];
        arr[1] = Math.max( nums[0], nums[1]);

        for( int i = 2; i<n; i++)
        {
            arr[i] = Math.max( (nums[i] + arr[i -2]), (arr[i - 1]) );
        }

        return arr[n - 1];
    }
}
```

→ Here initially we need to first tackle the edge cases and then we will go on to the loop.
→ The loop needs to stsrt from the 2nd element because we are always considering the n-1 and n-2th elements.
→ At the nth element we can either take the result of the  n-1th item + cost of the nth item OR the n-1th item.

### Memoization ( Recursive Approach )

→
