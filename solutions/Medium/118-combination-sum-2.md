# 118. combination sum 2

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Recursion |
| **Solved on** | 2026-08-24 |
| **How I got there** | Major Thinking required, Saw Video Soution |
| **Link** | [Problem link](https://leetcode.com/problems/combination-sum-ii/description/) |

---

## Problem

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

**Example 2:**

```
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```

**Constraints:**

* `1 <= candidates.length <= 100`
* `1 <= candidates[i] <= 50`
* `1 <= target <= 30`

## My Notes & Solution

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res =[]
        candidates.sort()

        def recurse( idx, curr,candidates, total):

            ## Base conditions
            if total == target :
                res.append( curr.copy())
                return
            
            if total > target or idx >= len(candidates):
                return
            
            ##pick
            curr.append(candidates[idx])
            recurse( idx + 1, curr, candidates, total + candidates[idx])

            ## undo
            curr.pop()

            ##backtrack
            while (idx + 1 < len(candidates)) and candidates[idx] == candidates[idx+1]:
                idx+=1

            recurse(idx + 1, curr, candidates, total)
        
        recurse( 0,[],candidates, 0)
        return res
            

```

- We need to sort the list as then we will be able to eliminate adjacent similar elements.

- There are 2 cases:

- If we are to unpick the element we first check whether the curr element is similar to the next or not.

- We then dont add the current position and just go over.

```python
Sort
  ↓
At each level:
  ├── Pick current element
  │     ↓
  │   Recurse
  │     ↓
  │   Undo choice
  │
  └── Don't Pick
        ↓
      Skip adjacent duplicates
        ↓
      Recurse
```

#### Key Concept to Remember

> Sorting + skipping adjacent duplicates prevents duplicate combinations.

And:

> Pick/Don't Pick controls the decision; backtracking restores the state after the Pick branch.
