# 088. Single element in Sorted Array

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Binary Search |
| **Solved on** | 2026-06-29 |
| **How I got there** | Saw Video Soution |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

- One thing we can assert is that if an element is in an even location and the similar element is present in the odd position adjacent to it then it is definitely in the left side of the array.

- If the element is in the odd location and the same element is adjacent to it then it is obviously in the right side.

- That element can be said to be a single element if the element on either side of it is dissimilar.

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        ## For this question we need to identify whether we are on the left or the right half
        ## Once we get those halves we just need to eliminate those halves.

        n = len(nums)
        if n == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[n-1] != nums[n-2]:
            return nums[n-1]

        n = len(nums)

        low = 1
        high = n - 2

        while( low <= high):

            mid = ( low + high )// 2
            if nums[mid] != nums[mid -1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            ## Now we need to check which side is it actually

            ## This checks for the entire left condition
            if ( mid % 2 == 0 and nums[mid] == nums[mid + 1] ) or ( mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                low = mid + 1
            
            ## This is eventually checking for the right side
            else:
                high = mid - 1

        return -1
```

Another implementation which is the brute force is the Frequency approach:

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = freq.get( nums[i], 0) + 1

        for key, value in freq.items():
            if freq[key] == 1:
                return key
        
        return -1
```
