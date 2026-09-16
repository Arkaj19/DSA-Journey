# 071. 2553. Separate the Digits in an Array

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Arrays, Strings |
| **Solved on** | 2026-05-11 |
| **How I got there** | Could solve it instantly |
| **Link** | [Problem link](https://leetcode.com/problems/separate-the-digits-in-an-array/description/?envType=daily-question&envId=2026-05-11) |

---

## Problem

Given an array of positive integers `nums`, return *an array* `answer` *that consists of the digits of each integer in* `nums` *after separating them in **the same order** they appear in* `nums`.

To separate the digits of an integer is to get all the digits it has in the same order.

* For example, for the integer `10921`, the separation of its digits is `[1,0,9,2,1]`.

**Example 1:**

```
Input: nums = [13,25,83,77]
Output: [1,3,2,5,8,3,7,7]
Explanation: 
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.
```

**Example 2:**

```
Input: nums = [7,1,3,9]
Output: [7,1,3,9]
Explanation: The separation of each integer in nums is itself.
answer = [7,1,3,9].
```

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 105`

## My Notes & Solution

```python
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = []

        for i in range( n):

            num = nums[i]
            s_num = str(num)

            for i in range( len(s_num)):
                ans.append(int(s_num[i]))
        
        return ans
```

- Its a very easy question where we just need to focus on the conversion of the integer value to string and then extracting the characters from it one by one. 

- The math version of it is a bit more complex. 

- Because we know that the modulus always gives us the last digit but here we want the first hence we will have to keep a temporary array and at the end we will reverse it and extend to the main ans array.

```python
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = []

        for i in range( n):

            num = nums[i]
            
            ### ---> Math Version <---

            temp = []

            while num > 0:
                digit = num % 10
                temp.append(digit)
                num = num // 10

            temp.reverse()

            ans.extend(temp) 
        
        return ans
```
