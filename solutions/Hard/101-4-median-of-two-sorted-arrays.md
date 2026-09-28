# 101. 4. Median of Two Sorted Arrays

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Hard |
| **Topics** | Binary Search |
| **Solved on** | 2026-08-04 |
| **How I got there** | Saw Video Soution, Major Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

Brute Force Solution

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums3 = []
        n1 = len(nums1)
        n2 = len(nums2)
        i = 0
        j = 0

        while ( i < n1 and j < n2):

            if nums1[i] <= nums2[j] :
                nums3.append(nums1[i])
                i+=1
            
            else:
                nums3.append(nums2[j])
                j+=1

        while( i < n1):
            nums3.append(nums1[i])
            i+=1

        while ( j < n2):
            nums3.append(nums2[j])
            j+=1

        print(nums3)

        n3 = n1 + n2

        if n3 % 2 >= 1:
            return nums3[n3 // 2]
        
        else:
            ans = (nums3[n3 // 2] + nums3[( n3 )// 2 - 1 ]) / 2
            return ans

```

Optimal Solution ( Binary Search )
