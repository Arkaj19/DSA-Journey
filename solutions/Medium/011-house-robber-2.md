# 011. House Robber 2 

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | DP |
| **Solved on** | 2026-03-23 |
| **How I got there** | Needed Hint from ChatGpt |
| **Link** | [Problem link](https://leetcode.com/problems/house-robber-ii/) |

---

## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

**Example 1:**

```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```

**Example 2:**

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

**Example 3:**

```
Input: nums = [1,2,3]
Output: 3
```

**Constraints:**

* `1 <= nums.length <= 100`
* `0 <= nums[i] <= 1000`

## My Notes & Solution

Its the same as that of the normal house robber problem.
The main difference is that : Here there will be two cases. Once we wont consider the first house and the next time we wont consider the last house.

→ then we will take out the max out of the results of the [n-1] values of both of them.
⇒ That will give us our result.

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        int arr1[] = new int[n-1]; // Will exclude the last house  
        int arr2[] = new int[n-1]; // Will exclude the first house

        if( nums.length == 1) // If the array has 1 element
        return nums[0];
        
        if( nums.length == 2) // If the array has 2 elements
        {
            return Math.max( nums[0], nums[1]);
        }

        // The change here is that we will take two cases at hand once we will remove the first and second we will remove the first element

        // 1. Removing the last house

        arr1[0] = nums[0];
        arr1[1] = Math.max( nums[0], nums[1]);
        for( int i = 2; i<n-1; i++)
        {
            arr1[i] = Math.max( (nums[i] + arr1[i - 2]), (arr1[i - 1]));
        }

        // 2. Removing the first house
        arr2[0] = nums[1];
        arr2[1] = Math.max( nums[1], nums[2]); 
        for( int i = 2; i<n-1; i++)
        {
            arr2[i] = Math.max( (nums[i+1] + arr2[i - 2]), (arr2[i - 1]));
        }

        return Math.max( arr1[n - 2], arr2[n - 2]);
    }
}
```
