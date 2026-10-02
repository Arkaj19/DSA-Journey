# 107. Find Peak Element

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Binary Search |
| **Solved on** | 2026-08-10 |
| **How I got there** | Saw Chatgpt Solution ( Code ), Needed Hint from ChatGpt |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            peak = max(nums)

            for i in range( len(nums)):
                if nums[i] == peak:
                    return i

        low = 0
        high = len(nums) - 1
        peak = -float('inf')

        while( low < high):

            mid = ( low + high)// 2

            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low
```

#### Peak Element (LeetCode 162)

- A peak element is an element that is greater than its neighbors.

- We do not search for the maximum element.

- Use the slope between nums[mid] and nums[mid+1].

#### Binary Search Logic

```plain text
nums[mid] < nums[mid+1]
```

➡ Increasing slope

➡ Peak exists on the right side

```plain text
low = mid + 1
```

---

```plain text
nums[mid] > nums[mid+1]
```

➡ Decreasing slope

➡ Peak exists at mid or on the left side

```plain text
high = mid
```

---

#### Why high = mid and not mid - 1?

- mid itself can be the peak.

- Do not discard a possible answer.

---

#### Loop Condition

```plain text
while low < high
```

- Keep shrinking the search space.

- When low == high, we have reached a peak.

---

#### Final Answer

```plain text
return low
```

because

```plain text
low == high
```

at the end.

---

#### Complexity

- Time: O(log n)

- Space: O(1)

---

#### Pattern Recognition

When the question says:

```plain text
Find a peak
Find a local maxima
Mountain-like structure
```

Think:

```plain text
Compare nums[mid] with nums[mid+1]
Use slope-based binary search
```

Key takeaway:

👉 Binary search is not finding the peak directly; it is finding the side where a peak is guaranteed to exist.
