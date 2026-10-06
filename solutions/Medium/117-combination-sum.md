# 117. Combination Sum

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Recursion |
| **Solved on** | 2026-08-20 |
| **How I got there** | Major Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

- Goal: Keep adding elements until the current sum reaches the target.

- At each recursive call, we have 3 possible conditions:

- The index can go beyond the size of the candidates array → stop the recursion.

- Add candidates[i] to the current sum.

- Append candidates[i] to the current combination.

- Recursively call the function.

- After the recursive call, pop the element to undo the previous choice.

- For the take case, stay at the same index because an element can be used multiple times.

- For the skip case, move to the next index using i + 1.

- Backtracking pattern:

```python
Add element
↓
Recursive call
↓
Pop element
↓
Try next possibility
```

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        l = []

        def solve ( i, candidates,sum, target, l):

            if sum == target:
                ans.append( l.copy())
                return 

            if i >= len(candidates):
                return 
            if sum > target:
                return 

            sum+=candidates[i]
            l.append(candidates[i])
            solve( i,candidates, sum, target, l)
            l.pop()
            solve(i+1, candidates, sum - candidates[i], target, l)
            


        solve(0,candidates,0,target, l)
        return ans
```
