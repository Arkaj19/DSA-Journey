# 065. Rotated Digits

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Arrays, Math |
| **Solved on** | 2026-05-02 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/rotated-digits/?envType=daily-question&envId=2026-05-02) |

---

## Problem

An integer `x` is a **good** if after rotating each digit individually by 180 degrees, we get a valid number that is different from `x`. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

* `0`, `1`, and `8` rotate to themselves,
* `2` and `5` rotate to each other (in this case they are rotated in a different direction, in other words, `2` or `5` gets mirrored),
* `6` and `9` rotate to each other, and
* the rest of the numbers do not rotate to any other number and become invalid.

Given an integer `n`, return *the number of **good** integers in the range* `[1, n]`.

**Example 1:**

```
Input: n = 10
Output: 4
Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
```

**Example 2:**

```
Input: n = 1
Output: 0
```

**Example 3:**

```
Input: n = 2
Output: 1
```

**Constraints:**

* `1 <= n <= 104`

## My Notes & Solution

```python
class Solution:
    def rotatedDigits(self, n: int) -> int:

        valid_arr = [2,5,6,9]
        invalid_arr = [3,7,4]
        count = 0
        good = False

        for i in range(1,n+1):

            good = False

            if i > 10:
                temp = i
                while temp != 0:
                        digit = temp % 10
                        if digit in invalid_arr:
                            good = False
                            break

                        if digit in valid_arr:
                            good = True

                        temp = temp // 10

                if good == True:
                    count+=1

            else:
                if i in valid_arr:
                    count+=1
        
        return count
```

- This is a very question. 

- If a number has numbers like 2,5,6,9 then that means a 2 if reversed becomes 5 or 6 ↔ 9 similarly

- Now these numbers are considered as true numbers.

- The numbers 3,4,7 these are considered invalid because they cannot be reversed.

- The numbers 0,1,8 are considered neutral because they change to themselves on being reversed 

- Now the thing is that if the number consists of all good and one neutral then also we will consider it good but if even a single bad number comes we will reject the number
