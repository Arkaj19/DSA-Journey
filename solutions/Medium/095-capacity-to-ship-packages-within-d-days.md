# 095. Capacity to ship Packages within D days

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Binary Search |
| **Solved on** | 2026-07-28 |
| **How I got there** | — |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low = max(weights)
        high = sum(weights)
        ans = float('inf')
        

        while( low <= high):

            mid = (low + high)// 2
            if self.capacity(weights, mid, days):
                ans = min(ans, mid)
                high = mid - 1
            
            else:
                low = mid + 1
            
        return ans

    def capacity(self, weights, mid, days):

        sum = 0
        allowed_days = 1
        for w in weights:
                
            if sum+w <= mid:
                sum+=w
            else:
                if days > 0:
                    allowed_days+=1
                    sum = w

        if days >= allowed_days:
            return True
        else:
            return False

```

#### Search Space

- low = max(weights) → Capacity cannot be less than the heaviest package.

- high = sum(weights) → One trip carrying all packages.

#### Feasibility Function

- Simulate shipping with a given capacity.

- Return True if all packages can be shipped within days, else **False`.

#### Simulation

- Maintain:

- If current_load + weight <= capacity:

- Else:

#### Binary Search

- If capacity is feasible:

- Else:

#### Common Mistakes

- ❌ Check current_load <= capacity

- ✅ Check current_load + weight <= capacity

- ❌ days_used = 0

- ✅ days_used = 1

- ❌ current_load = 0 after overflow

- ✅ current_load = weight

- ❌ Modify input days

- ✅ Maintain a separate days_used counter.

#### Template

1. Find search space.

1. Write a feasibility function.

1. Binary search on the answer.

1. If feasible → search left.

1. Else → search right.
