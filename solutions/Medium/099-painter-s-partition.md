# 099. Painter’s Partition

| | |
|---|---|
| **Platform** | GFG |
| **Difficulty** | Medium |
| **Topics** | Binary Search |
| **Solved on** | 2026-08-04 |
| **How I got there** | Major Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def minTime (self, arr, k):
        # code here

        low = max(arr)
        high = sum(arr)
        ans = float('inf')

        ## Considering that the lowest time possible is that of the largest piece of board since 1 unit of board takes 1 unit time
        
        while( low <= high):
            
            mid = (low + high) // 2
            
            if self.check( arr, mid, k):
                
                ans = min( mid, ans)
                high = mid - 1
            
            else:
                low = mid + 1
                
        return ans
        
    
    def check( self, arr, mid, k):
        
        count = 1
        sum = 0
        
        for i in range( len(arr) ):
            
            if sum + arr[i] <= mid :
                
                sum+= arr[i]
            
            else:
                count+=1
                sum = arr[i]
        
        if count <= k:
            return True
        
        else:
            return False
                
```

- This question is very similar to the book allocation problem.

- Lowest limit : The fastest all can complete a task is the size of the largest block because a minimum of that much time is required.

- High limit : The latest is that the summation of all the lengths of the boards.

- Finally we do the normal binary search and if our mid value satisfies our helper function then we try to check the time less than the current mid.

- This means that hypothetically if 4 workers complete a piece of work in 30 mins then can they complete it in 25 mins. ( try )

- Hence we have used a helper condition to check that

#### Painter's Partition – Revision Notes

- Same pattern as Allocate Minimum Pages (Board → Book, Painter → Student, Time → Pages).

- Low = max(arr): A painter must paint the largest board, so the minimum possible time is the length of the largest board.

- High = sum(arr): One painter paints all the boards.

- Binary search on the answer (time).

- Helper function: Can all boards be painted within mid time using at most k painters?

- If the helper returns True, store mid and search left (try a smaller time).

- If the helper returns False, search right (increase the allowed time).

#### Mental Model

> If the work can be completed in 30 minutes, can it also be completed in 25 minutes?
