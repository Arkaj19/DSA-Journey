# 050. Sum Of Distances

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Hashing, Two Pointers, Prefix Sum |
| **Solved on** | 2026-04-23 |
| **How I got there** | — |
| **Link** | [Problem link](https://leetcode.com/problems/sum-of-distances/description/) |

---

## Problem

You are given a **0-indexed** integer array `nums`.

There exists an array `arr` of length `nums.length`, where `arr[i]` is the sum of `|i - j|` over all `j` such that `nums[j] == nums[i]` and `j != i`. If there is no such `j`, set `arr[i]` to be 0.

Return the array `arr`.

**Example 1:**

```
Input: nums = [1,3,1,1,2]
Output: [5,0,3,4,0]
Explanation: 
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
When i = 4, arr[4] = 0 because there is no other index with value 2.
```

**Example 2:**

```
Input: nums = [0,5,3]
Output: [0,0,0]
Explanation: Since each element in nums is distinct, arr[i] = 0 for all i.
```

**Constraints:**

* `1 <= nums.length <= 105`
* `0 <= nums[i] <= 109`

**Note:** This question is the same as  [2121: Intervals Between Identical Elements.](https://leetcode.com/problems/intervals-between-identical-elements/description/)

## My Notes & Solution

```python
from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        n = len(nums)
        sum = []
        curr_sum = 0

        for i in range(n):
            curr = nums[i]
            curr_sum = 0

            for j in range(0,n):
                if nums[i] == nums[j] and i!=j:
                    curr_sum+= abs( i - j)
            
            sum.append(curr_sum)

        return sum
```

- This is the brute force and it throws TLE so dont use it

## Optimized Solution

- We will be using prefix sum here

- We will have to get 4 things :

- Here once we traverse from left to right and then we come back from right to left and at the end we add all the values of left to right in the resultant array

```javascript
class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        count_mp = {}
        sum_mp = {}
        n = len(nums)
        
        ## Left to right
        arr_left = []

        for i in range(n):

            count_mp[nums[i]] = count_mp.get(nums[i],0)+1 # Here we are getting the frequencies of nums[i]
            sum_mp[nums[i]] = sum_mp.get(nums[i], 0) + i # Here we are getting the sum of indices of nums[i]

            # Here we are getting the values of the left array
            arr_left.append( i * count_mp[nums[i]] - sum_mp[nums[i]]) 
        
        count_mp.clear()
        sum_mp.clear()

        ## Right to left
        arr_right = []

        for idx,val in enumerate(nums[::-1]):

            i = n - 1 - idx  ## Essentially we are doing 0 -> 4 idx conversion 

            count_mp[val] = count_mp.get(val,0)+1
            sum_mp[val] = sum_mp.get(val,0) + i

            # THis is reversed because the values of the right array as it is normally (3 - 4 which will be -ve)
            arr_right.append( sum_mp[val] - i * count_mp[val])
        
        arr_right.reverse()

        ## Finally calculating result
        res = []
        
        for k in range(n):
            res.append(arr_left[k] + arr_right[k])
        
        return res
```
