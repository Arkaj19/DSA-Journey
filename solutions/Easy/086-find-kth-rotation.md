# 086. Find Kth Rotation

| | |
|---|---|
| **Platform** | GFG |
| **Difficulty** | Easy |
| **Topics** | Binary Search |
| **Solved on** | 2026-06-26 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://www.geeksforgeeks.org/problems/rotation4723/1) |

---

## Problem

_Couldn't auto-fetch the statement (paid-only question, or the source page changed). See the [original link](https://www.geeksforgeeks.org/problems/rotation4723/1)._

## My Notes & Solution

```python
class Solution:
    def findKRotation(self, arr):
        # code here
        
        num = min(arr)
        rotation = 0
        
        for i in range(len(arr) - 1):
            if arr[i] == num:
                break
            else:
                rotation+=1
        
        return rotation
```
