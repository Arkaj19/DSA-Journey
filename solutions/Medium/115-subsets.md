# 115. Subsets

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Recursion |
| **Solved on** | 2026-08-19 |
| **How I got there** | Major Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/subsets/) |

---

## Problem

Given an integer array `nums` of **unique** elements, return *all possible* *subsets* *(the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2:**

```
Input: nums = [0]
Output: [[],[0]]
```

**Constraints:**

* `1 <= nums.length <= 10`
* `-10 <= nums[i] <= 10`
* All the numbers of `nums` are **unique**.

## My Notes & Solution

Discussion:

- Pick / Unpick (Take / Don't Take) concept

- At each recursion level, make a decision about the current element: pick it or don't pick it.

- res is a mutable list, so append() modifies the same list object.

- Because the same res is shared between recursive branches, after exploring the pick branch, we must undo the choice using res.pop() before exploring the don't-pick branch.

- This follows the general backtracking pattern:Make → Explore → Undo

- At the base case, use res.copy() when storing the result because res will continue to be modified after the recursive call returns. Without copying, multiple result entries can reference the same mutable list.

Notes:

1. Had we done res + [num] it would have created a new list, so the original res was never modified → no pop() needed.

Template:

```python
class Solution:
    arr = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.arr = []
        self.find_subsets([], nums)
        return self.arr
        
    def find_subsets( self, res, nums ):

        if len(nums) == 0:
            self.arr.append(res)
            res = []
            return 

        # Take the first element
        num = nums[0]
        res.append(num)
        self.find_subsets( res, nums[1:])

        ##bakctrack
        res.pop()

        ## Dont take 
        self.find_subsets( res, nums[1:])
```
