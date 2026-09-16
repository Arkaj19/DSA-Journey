# 073. 2848. Points That Intersect With Cars

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Arrays, Boolean array formation |
| **Solved on** | 2026-05-13 |
| **How I got there** | Major Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/points-that-intersect-with-cars/) |

---

## Problem

You are given a **0-indexed** 2D integer array `nums` representing the coordinates of the cars parking on a number line. For any index `i`, `nums[i] = [starti, endi]` where `starti` is the starting point of the `ith` car and `endi` is the ending point of the `ith` car.

Return *the number of integer points on the line that are covered with **any part** of a car.*

**Example 1:**

```
Input: nums = [[3,6],[1,5],[4,7]]
Output: 7
Explanation: All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.
```

**Example 2:**

```
Input: nums = [[1,3],[5,8]]
Output: 7
Explanation: Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8. There are a total of 7 points, therefore the answer would be 7.
```

**Constraints:**

* `1 <= nums.length <= 100`
* `nums[i].length == 2`
* `1 <= starti <= endi <= 100`

## My Notes & Solution

```python
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        n = len(nums)
        arr = [False] * 101
        
        for i in range(n):

            # print(nums[i][0], nums[i][1])
            for j in range( nums[i][0], nums[i][1] + 1):
                # print(j)
                if arr[j] == True:
                    pass
                else:
                    arr[j] = True

        count = 0

        for i in range(1,len(arr)):
            # print(i)
            if arr[i] == True:
                count+=1

        return count
```

- Then I take a boolean array of 100 length and initialize with False at all places.

- Then we just go over the main nums array and then we check all the points for each pair and mark them true.

- Finally we run another for loop which goes over the 101 size array and counts the number of true positions for us and its done.

```python
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        n = len(nums)
        arr = [False] * 101

        for i in range(n):

            # print(nums[i][0], nums[i][1])
            for j in range( nums[i][0], nums[i][1] + 1):
                # print(j)
                if arr[j] == True:
                    pass
                else:
                    arr[j] = True

        return sum(arr)
```

- Here we changed the last for loop with the sum function because it works the same by counting the number of true points and returning it.
