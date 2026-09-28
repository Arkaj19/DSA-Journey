# 100. 410. Split Array Largest Sum

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Hard |
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
    def splitArray(self, nums: List[int], k: int) -> int:

        low = max(nums)
        high = sum(nums)
        ans = float('inf')

        while( low <= high):

            mid = ( low + high) // 2
            if self.check( nums, mid, k):

                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
        
    def check( self,arr,mid,k):

        sum = 0
        count = 1

        for i in range( len(arr)):

            if sum + arr[i] <= mid:
                sum+= arr[i]
            
            else:
                sum = arr[i]
                count+=1

        if count <= k:
            return True
        else:
            return False

```

### 410. Split Array Largest Sum – Revision Notes

- Pattern: Same as Allocate Minimum Pages, Painter's Partition, and Ship Packages.

- Goal: Minimize the maximum subarray sum.

- Do not sort the array because subarrays must remain contiguous.

#### Search Space

- low = max(nums) → Every subarray must contain its largest element.

- high = sum(nums) → One subarray containing all elements.

#### Helper Function

- Given a maximum allowed subarray sum (mid), count how many subarrays are needed.

- Maintain:

- If current_sum + nums[i] <= mid:

- Else:

#### Binary Search

- If subarrays_used <= k:

- Else:

#### Key Insight

> For every possible split, compute the largest subarray sum.

#### Common Mistakes

- ❌ Sorting the array.

- ❌ Using < instead of <= when checking if an element fits.

- ❌ Resetting current_sum to 0 after overflow.

- ✅ Start the new subarray with the current element (current_sum = nums[i]).

- ❌ Checking subarrays_used == k.

- ✅ Check subarrays_used <= k.
