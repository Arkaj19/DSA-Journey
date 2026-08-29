# 032. Minimum Absolute Distance Between Mirror Pairs

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Arrays |
| **Solved on** | 2026-04-17 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/description/) |

---

## Problem

You are given an integer array `nums`.

A **mirror pair** is a pair of indices `(i, j)` such that:

* `0 <= i < j < nums.length`, and
* `reverse(nums[i]) == nums[j]`, where `reverse(x)` denotes the integer formed by reversing the digits of `x`. Leading zeros are omitted after reversing, for example `reverse(120) = 21`.

Return the **minimum** absolute distance between the indices of any mirror pair. The absolute distance between indices `i` and `j` is `abs(i - j)`.

If no mirror pair exists, return `-1`.

**Example 1:**

**Input:** nums = [12,21,45,33,54]

**Output:** 1

**Explanation:**

The mirror pairs are:

* (0, 1) since `reverse(nums[0]) = reverse(12) = 21 = nums[1]`, giving an absolute distance `abs(0 - 1) = 1`.
* (2, 4) since `reverse(nums[2]) = reverse(45) = 54 = nums[4]`, giving an absolute distance `abs(2 - 4) = 2`.

The minimum absolute distance among all pairs is 1.

**Example 2:**

**Input:** nums = [120,21]

**Output:** 1

**Explanation:**

There is only one mirror pair (0, 1) since `reverse(nums[0]) = reverse(120) = 21 = nums[1]`.

The minimum absolute distance is 1.

**Example 3:**

**Input:** nums = [21,120]

**Output:** -1

**Explanation:**

There are no mirror pairs in the array.

**Constraints:**

* `1 <= nums.length <= 105`
* `1 <= nums[i] <= 109`​​​​​​​

## My Notes & Solution

```python
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        num_dict = {}
        ans = []

        for idx,num in enumerate(nums):

            # First access a number and check if it exists in the dict or not
            # If not then create a num_dict with the reverse of that num and its index

            if num not in num_dict:
                curr_string = str(num)
                rev_curr = curr_string[::-1]
                rev_num = int(rev_curr)

                num_dict[rev_num] = idx
            
            else:
                dist = abs(idx - num_dict[num])
                ans.append(dist)

        if len(ans) > 0:
            return min(ans)
        else:
            return -1
```

- With this code I got a TLE and thats because if the element was not present in the num_dict we were

- Converting it to string → reversed it → converted back to int → Stored it

- But we had forgotten to also do the same for the ones present in the num_dict that they also need to be reversed.

### Correct Version

```python
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        num_dict = {}
        ans = []

        for idx,num in enumerate(nums):

            # First access a number and check if it exists in the dict or not
            # If not then create a num_dict with the reverse of that num and its index

            if num not in num_dict:
                curr_string = str(num)
                rev_curr = curr_string[::-1]
                rev_num = int(rev_curr)

                num_dict[rev_num] = idx
            
            else:
                dist = abs(idx - num_dict[num])
                ans.append(dist)

                curr_string = str(num)
                rev_curr = curr_string[::-1]
                rev_num = int(rev_curr)
                num_dict[rev_num] = idx
            
        print(num_dict)
        print(len(num_dict))

        if len(ans) > 0:
            return min(ans)
        else:
            return -1
```
