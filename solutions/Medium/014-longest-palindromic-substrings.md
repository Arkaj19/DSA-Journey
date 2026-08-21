# 014. Longest Palindromic Substrings

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | DP |
| **Solved on** | 2026-04-01 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/longest-palindromic-substring/) |

---

## Problem

Given a string `s`, return *the longest* *palindromic* *substring* in `s`.

**Example 1:**

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

**Example 2:**

```
Input: s = "cbbd"
Output: "bb"
```

**Constraints:**

* `1 <= s.length <= 1000`
* `s` consist of only digits and English letters.

## My Notes & Solution

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        cols = rows = n
        dp = [[-1]*(cols) for _ in range( rows)]
        max_size = 1
        res = ''
        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                max_size = 2
            else:
                dp[i][i+1] = 0

        for length in range(3,n+1):
            for start in range(n-length+1):
                end = start + length - 1
                if s[start] == s[end] and dp[start+1][end - 1] == 1:
                    dp[start][end] = 1
                    max_size = max(max_size,end - start + 1)
                else:
                    dp[start][end] = 0

        for i in range(n - max_size + 1):
            if dp[i][i + max_size - 1] == 1:
                res = s[i:i + max_size]
                break
            
        return res
```

→ Here the only new thing is that I am taking out the max_length of the palindromic substring first.
→ This is because I know that if I have the max_length then I can check for the simultaneous strings of that length and can return the same answer.
