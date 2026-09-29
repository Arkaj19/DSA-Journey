# 102. Minimize Max Distance of Adjacent Gas Stations

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Hard |
| **Topics** | Binary Search |
| **Solved on** | 2026-08-05 |
| **How I got there** | Major Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def minMaxDist(self, stations, k):
        # Code here
        if len(stations) < 2:
            return 0.0
        
        low = 1e-6
        high = -float('inf')
        
        for i in range( len(stations) - 1):

            high = max( high, (stations[i + 1] - stations[i]) )

        ans = high
        
        while( high - low > 1e-6):

            mid = ( low + high) / 2

            if self.check(stations,mid,k):

                ans = min( ans, mid)
                high = mid
            
            else:
                low = mid
        
        return ans


    def check( self, stations, mid, k):

        station_count = 0

        for i in range( len(stations) - 1):

            gap = stations[i+1] - stations[i]
            # pieces = int(gap / mid)
            # if gap % mid == 0:
            #     station_count+= ( pieces - 1)
            
            # else:
            #     station_count+= pieces
            station_count += int(gap / mid) 

        if station_count <= k:
            return True
        else:
            return False

```
