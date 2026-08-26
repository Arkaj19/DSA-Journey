# 027. Valid Palindrome 2

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Strings |
| **Solved on** | 2026-04-14 |
| **How I got there** | — |
| **Link** | [Problem link](https://leetcode.com/problems/valid-palindrome-ii/description/) |

---

## Problem

Given a string `s`, return `true` *if the* `s` *can be palindrome after deleting **at most one** character from it*.

**Example 1:**

```
Input: s = "aba"
Output: true
```

**Example 2:**

```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

**Example 3:**

```
Input: s = "abc"
Output: false
```

**Constraints:**

* `1 <= s.length <= 105`
* `s` consists of lowercase English letters.

## My Notes & Solution

- Below solution came out of my head which is the most basic implementation hence it throws TLE but it is written in Recursive solution.

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        n = len(s)
        return self.check(s,n-1)

    def check(self,s,num):

        if num < 0:
            return False

        st = ""
        for i,ch in enumerate(s):
            if i != num:
                st += ch

        if st == st[::-1]:
            return True
        else:
            return self.check( s,num - 1)
```

-
