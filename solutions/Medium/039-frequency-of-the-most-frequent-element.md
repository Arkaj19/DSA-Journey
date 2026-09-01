# 039. Frequency of the Most Frequent Element

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Two Pointers |
| **Solved on** | 2026-04-20 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/) |

---

## Problem

The **frequency** of an element is the number of times it occurs in an array.

You are given an integer array `nums` and an integer `k`. In one operation, you can choose an index of `nums` and increment the element at that index by `1`.

Return *the **maximum possible frequency** of an element after performing **at most*** `k` *operations*.

**Example 1:**

```
Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
```

**Example 2:**

```
Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
```

**Example 3:**

```
Input: nums = [3,9,6], k = 2
Output: 1
```

**Constraints:**

* `1 <= nums.length <= 105`
* `1 <= nums[i] <= 105`
* `1 <= k <= 105`

## My Notes & Solution

```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)
        left = 0
        right = 0

        max_window = 0
        sum = 0
        
        while right < n :
            sum+=nums[right]
            window_size = right - left + 1

            while nums[right] * window_size - sum > k:
                sum-= nums[left]
                left+=1
                window_size = right - left + 1

            max_window = max(max_window, window_size)
            right+=1

        
        return max_window
```

- Here instead of blindly trying to store the frequencies or changing we can just maintain a prefix sum of each number.

- We will be maintaining a window and a sum .

- THe formula is :

```python
nums[right] * window_size - sum > k
```

- If this function satisfies then that means the window is valid and we need to shrink it at the earliest.

- We first remove the leftmost element from the sum and then remove the leftmost element.

- Then we also re-calculate the window size again. 

- Finally we find the max_window size and increase the right by 1 .

- Finally we return the maximum window size.
