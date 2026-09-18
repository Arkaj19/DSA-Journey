# 076. 3120. Count the Number of Special Characters I

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Arrays, Sets |
| **Solved on** | 2026-05-27 |
| **How I got there** | — |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        chars = set("abcdefghijklmnopqrstuvwxyz")

        count = 0
        s = set(word)

        for curr in chars:

            if curr.lower() in s and curr.upper() in s:
                count+=1
        
        return count
```
