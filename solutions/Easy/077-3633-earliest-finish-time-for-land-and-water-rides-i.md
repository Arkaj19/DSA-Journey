# 077. 3633. Earliest Finish Time for Land and Water Rides I

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Arrays, Greedy, Nested For |
| **Solved on** | 2026-06-02 |
| **How I got there** | Minor Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        l = len(landStartTime)
        w = len(waterStartTime)
        i = 0
        j = 0
        min_time = float('inf')

        for i in range(l):
            for j in range(w):

                ## Land -> Water
                land_time = landStartTime[i] + landDuration[i]
                land_start_total = max(land_time,waterStartTime[j]) + waterDuration[j]

                min_time = min(min_time, land_start_total)

                ## Water -> Land

                water_time = waterStartTime[j] + waterDuration[j]
                water_start_time = max(landStartTime[i],water_time) + landDuration[i]

                min_time = min(min_time, water_start_time)

        
        return min_time
```

- Here we need to know the path can be both water → land or land → water. 

- This is to see which finished first.

- One optimized thing is that if we know that there can be a wait time if there is time to start between two rides then we can take the max() of the end time and the next ride start time.

- It will remove an unnecessary if-else loop.
