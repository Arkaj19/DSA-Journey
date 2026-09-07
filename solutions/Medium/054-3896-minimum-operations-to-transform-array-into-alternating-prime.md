# 054. 3896. Minimum Operations to Transform Array into Alternating Prime

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Math |
| **Solved on** | 2026-04-23 |
| **How I got there** | Major Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/) |

---

## Problem

You are given an integer array `nums`.

An array is considered **alternating prime** if:

* Elements at **even** indices (0-based) are **prime** numbers.
* Elements at **odd** indices are **non-prime** numbers.

In one operation, you may **increment** any element by 1.

Return the **minimum** number of operations required to transform `nums` into an **alternating prime** array.

A **prime** number is a natural number greater than 1 with only two factors, 1 and itself.

**Example 1:**

**Input:** nums = [1,2,3,4]

**Output:** 3

**Explanation:**

* The element at index 0 must be prime. Increment `nums[0] = 1` to 2, using 1 operation.
* The element at index 1 must be non-prime. Increment `nums[1] = 2` to 4, using 2 operations.
* The element at index 2 is already prime.
* The element at index 3 is already non-prime.

Total operations = `1 + 2 = 3`.

**Example 2:**

**Input:** nums = [5,6,7,8]

**Output:** 0

**Explanation:**

* The elements at indices 0 and 2 are already prime.
* The elements at indices 1 and 3 are already non-prime.

No operations are needed.

**Example 3:**

**Input:** nums = [4,4]

**Output:** 1

**Explanation:**

* The element at index 0 must be prime. Increment `nums[0] = 4` to 5, using 1 operation.
* The element at index 1 is already non-prime.

Total operations = 1.

**Constraints:**

* `1 <= nums.length <= 105`
* `1 <= nums[i] <= 105`

## My Notes & Solution

```python
class Solution:
    def minOperations(self, nums: list[int]) -> int:

        count = 0
        max_num = max(nums) + 1000
        arr = self.prime( max_num)

        for idx,num in enumerate(nums):
            
            # odd
            if idx % 2 != 0: 
                while arr[num]:
                    count+=1
                    num+=1

            ## Even
            else: 
                while not arr[num]:
                    num+=1
                    count+=1

        return count

    def prime( self,max_num):

        arr = [True] * ( max_num + 1)
        arr[0] = arr[1] = False

        for i in range(2, int( max_num ** 0.5 ) + 1 ):
            if arr[i] == True:
                #Marking multiples of i starting from i*i
                for j in range( i*i, max_num + 1, i):
                    arr[j] = False

        return arr
```

- Here the catch is that to find the prime numbers we can initially create an array of numbers of all uptil the max number

-
