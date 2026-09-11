# 061. Find the middle index of the array

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Prefix Sum |
| **Solved on** | 2026-04-26 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/find-the-middle-index-in-array/submissions/1988844713/) |

---

## Problem

Given a **0-indexed** integer array `nums`, find the **leftmost** `middleIndex` (i.e., the smallest amongst all the possible ones).

A `middleIndex` is an index where `nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1]`.

If `middleIndex == 0`, the left side sum is considered to be `0`. Similarly, if `middleIndex == nums.length - 1`, the right side sum is considered to be `0`.

Return *the **leftmost*** `middleIndex` *that satisfies the condition, or* `-1` *if there is no such index*.

**Example 1:**

```
Input: nums = [2,3,-1,8,4]
Output: 3
Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4
```

**Example 2:**

```
Input: nums = [1,-1,4]
Output: 2
Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0
```

**Example 3:**

```
Input: nums = [2,5]
Output: -1
Explanation: There is no valid middleIndex.
```

**Constraints:**

* `1 <= nums.length <= 100`
* `-1000 <= nums[i] <= 1000`

**Note:** This question is the same as 724: <https://leetcode.com/problems/find-pivot-index/>

## My Notes & Solution

```python
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        n = len(nums)

        ## Created the two prefix and suffix arrays
        left_sum = [0] * n
        right_sum = [0] * n

        ## Initialized the 0th and (n-1)th index elements 
        left_sum[0] = nums[0]
        right_sum[n-1] = nums[n-1]

        ##Initially check if the array is of just 1 length then we will just return the 0th index
        if n == 1:
            return 0

        ## Fill up the prefix sum array
        for i in range(1,n):
            left_sum[i] = nums[i] + left_sum[i-1]

        ## Filled the suffix array
        for i in range(n-2,-1,-1):
            right_sum[i] = nums[i] + right_sum[i+1]

        ## Now we will be checking the index which will have the left_sum[i-1] and right_sum[i+1] as same

        for i in range(0,n):
						
            if i == 0:
                if right_sum[i+1] == 0:
                    return i
                else:
                    continue

            if i == n - 1:
                if left_sum[i-1] == 0:
                    return i
                else:
                    continue

            if left_sum[i-1] == right_sum[i+1]:
                return i

        return -1
```

- These 2 conditions are very important

```python
if i == 0:
    if right_sum[i+1] == 0:
        return i
    else:
        continue

if i == n - 1:
    if left_sum[i-1] == 0:
        return i
    else:
        continue
```

- This is because if the i == 0 then the left_sum[i-1] will give us index out of bounds error and same for the n-1th value as its right_Sum[i+1] will give the same error

- If the sum is 0 on the right hand side like in this case.

```plain text
[ 1, 2, -2 ] 

--> Hence here if we see that the sum on the right side of 1 is 0 ( as +2 -2 = 0 )
--> Hence in this case the 0th element is the pivot for us
```

- Rest the code is an easy code using Prefix and suffix sum
