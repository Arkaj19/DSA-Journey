# 120. Permutations

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Recursion |
| **Solved on** | 2026-08-26 |
| **How I got there** | Major Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/permutations/) |

---

## Problem

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2:**

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

**Example 3:**

```
Input: nums = [1]
Output: [[1]]
```

**Constraints:**

* `1 <= nums.length <= 6`
* `-10 <= nums[i] <= 10`
* All the integers of `nums` are **unique**.

## My Notes & Solution

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def find_perm( idx, curr):

            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(0, len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    find_perm(i + 1, curr)
                
                else:
                    continue

                curr.pop()
        
        find_perm( 0,[])
        return res
```

### Permutations — Revision Notes

- Base condition: When curr contains all elements, it represents one complete permutation → save it.

- Why a loop? At every level, any unused element can be the next choice, so we need to explore multiple choices.

- Core state: Track which elements are already used, not the previous element or index.

- For each candidate:

- Backtracking: After returning from recursion, undo the choice ( i.e. pop the element ) so the same element can be considered in another branch.

#### Core intuition

> Permutation = choose any unused element at every level.

```plain text
Multiple choices
      ↓
Choose unused element
      ↓
Recurse
      ↓
Undo choice
      ↓
Try next unused element
```

Combination: availability is controlled by index.

Permutation: availability is controlled by used state.
