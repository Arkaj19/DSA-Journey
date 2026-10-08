# 121. Subsets  2

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Recursion |
| **Solved on** | 2026-08-27 |
| **How I got there** | Major Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
    
        def subsets( idx, curr):

            if idx == len(nums):
                if curr not in res:
                    res.append(curr.copy())
                    return
                else:
                    return
            
            curr.append(nums[idx])
            subsets(idx + 1, curr)

            ##Pop the element 
            curr.pop()

            ## Backtrack
            subsets( idx + 1, curr)

        subsets( 0, [])
        return res


            
```

Subsets

```plain text
Take / Don't Take
```

Combinations

```plain text
Loop from start index
→ Pick
→ Recurse(i + 1)
→ Pop
```

Permutations

```plain text
Loop through ALL elements
→ Skip used
→ Pick
→ Recurse
→ Unpick
```

Then the "II" versions generally add:

```plain text
Duplicates → sort + skip duplicate choices at the appropriate recursion level
```

That's a much more repeatable framework than memorizing individual LeetCode solutions
