# 035. Mirror Distance of an Integer

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Strings |
| **Solved on** | 2026-04-18 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/mirror-distance-of-an-integer/description/?envType=daily-question&envId=2026-04-18) |

---

## Problem

You are given an integer `n`.

Define its **mirror distance** as: `abs(n - reverse(n))`​​​​​​​ where `reverse(n)` is the integer formed by reversing the digits of `n`.

Return an integer denoting the mirror distance of `n`​​​​​​​.

`abs(x)` denotes the absolute value of `x`.

**Example 1:**

**Input:** n = 25

**Output:** 27

**Explanation:**

* `reverse(25) = 52`.
* Thus, the answer is `abs(25 - 52) = 27`.

**Example 2:**

**Input:** n = 10

**Output:** 9

**Explanation:**

* `reverse(10) = 01` which is 1.
* Thus, the answer is `abs(10 - 1) = 9`.

**Example 3:**

**Input:** n = 7

**Output:** 0

**Explanation:**

* `reverse(7) = 7`.
* Thus, the answer is `abs(7 - 7) = 0`.

**Constraints:**

* `1 <= n <= 109`

## My Notes & Solution

```python
class Solution:
    def mirrorDistance(self, n: int) -> int:
        
        text = str(n)
        reverse_text = text[::-1]

        num = int(reverse_text)

        return abs(num - n)
```

- This doesn’t even requires any explanation.

- It is that easy..

Steps:

1. First convert to string

1. Reverse the string

1. Convert to int.

1. Find difference of the reversed int value and the normal value and return it.
