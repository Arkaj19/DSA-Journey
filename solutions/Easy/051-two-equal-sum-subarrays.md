# 051. Two Equal Sum Subarrays

| | |
|---|---|
| **Platform** | GFG |
| **Difficulty** | Easy |
| **Topics** | Prefix Sum |
| **Solved on** | 2026-04-23 |
| **How I got there** | Needed Hint from ChatGpt |
| **Link** | [Problem link](https://www.geeksforgeeks.org/problems/split-an-array-into-two-equal-sum-subarrays/1) |

---

## Problem

_Couldn't auto-fetch the statement (paid-only question, or the source page changed). See the [original link](https://www.geeksforgeeks.org/problems/split-an-array-into-two-equal-sum-subarrays/1)._

## My Notes & Solution

```python
  class Solution:
	def canSplit(self, arr):
			#code here
	    sum = 0
	
	    for num in arr:
	        sum+=num
	
	    if sum % 2 != 0:
	        return False
	
	    target = sum // 2
	    curr_sum = 0
	
	    n  = len(arr)
	
	    for i in range(n-1):
	        curr_sum+=arr[i]
	
	        if curr_sum == target:
	            return True
	
	    return False
```

- Here the most important thing is that this is a question of prefix sum and not two pointers

- It might feel to be two pointers in the beginning but it is to be done with prefix sum.

- The thing is that if while using two pointer a point comes when the both side sum becomes equal but it is not sure that the entire array is traversed then it can be a problem

-
