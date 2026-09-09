# 056. Buildings with Sunlight

| | |
|---|---|
| **Platform** | GFG |
| **Difficulty** | Easy |
| **Topics** | Math |
| **Solved on** | 2026-04-24 |
| **How I got there** | Could solve it instantly |
| **Link** | [Problem link](https://www.geeksforgeeks.org/problems/buildings-receiving-sunlight3032/1) |

---

## Problem

_Couldn't auto-fetch the statement (paid-only question, or the source page changed). See the [original link](https://www.geeksforgeeks.org/problems/buildings-receiving-sunlight3032/1)._

## My Notes & Solution

```python
class Solution:
    def visibleBuildings(self, arr):
        # code here
        
        curr_max = arr[0]
        count_building = 1
        
        for i in range( 1,len(arr)):
            
            if arr[i] >= curr_max:
                count_building+=1
                curr_max = arr[i]
                
        return count_building
            
```

- Here basically we need to check the curr_maximum value for each building at all times and  that will give us our result.
