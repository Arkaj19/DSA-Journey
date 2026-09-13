# 066. Rotate String

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Strings |
| **Solved on** | 2026-05-03 |
| **How I got there** | Could solve it instantly |
| **Link** | [Problem link](i dint get this) |

---

## Problem

_Couldn't auto-fetch the statement (paid-only question, or the source page changed). See the [original link](i dint get this)._

## My Notes & Solution

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        n = len(s)
        new_s = ""
        for i in range( 0, n):

            new_s = s[i+1: n] + s[0:i+1]
            print(new_s)
            if new_s == goal:
                return True
        
        return False

```

- The solution is very basic
