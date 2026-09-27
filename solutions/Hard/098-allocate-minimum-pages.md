# 098. Allocate Minimum Pages

| | |
|---|---|
| **Platform** | GFG |
| **Difficulty** | Hard |
| **Topics** | Binary Search |
| **Solved on** | 2026-08-03 |
| **How I got there** | Saw Video Soution, Major Thinking required, Needed Hint from ChatGpt |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def findPages(self, arr, k):
        # code here
        if len(arr) < k:
            return -1
            
        low = max(arr)
        high = sum(arr)
        ans = -float('inf')
        
        while( low <= high):
            
            mid = (low + high)// 2
            if self.check( arr, mid, k):
                ans = mid
                high = mid - 1
            
            else:
                low = mid + 1
                
        return ans
        
    
    def check(self, arr, mid, k):
        
        count = 1
        pages = 0
        
        for i in range( len(arr)):
            
            if pages + arr[i] <= mid and i < len(arr):
                pages+=arr[i]
                
            else:
                count+=1
                pages = arr[i]
        
        if count <= k:
            return True
        else:
            return False
```

### Binary Search on Answer – Allocate Minimum Pages

#### Search Space

- low = max(arr) → A student must be able to take the largest book.

- high = sum(arr) → One student takes all books.

#### Feasibility Function

- Simulate allocation for a given mid (maximum pages per student).

- Count students required.

- Return True if students_used <= k.

#### Simulation Logic

- students_used = 1

- current_pages = 0

- If current_pages + book <= mid:

- Else:

#### Binary Search

- If feasible:

- Else:

#### Common Mistakes

- ❌ current_pages <= mid

- ✅ current_pages + book <= mid

- ❌ current_pages = 0 after overflow

- ✅ current_pages = current_book

- ❌ Check students_used == k

- ✅ Check students_used <= k

- ❌ ans = max(ans, mid)

- ✅ ans = mid (or return low depending on implementation)
