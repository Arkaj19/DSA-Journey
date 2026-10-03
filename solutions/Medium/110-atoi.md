# 110. atoi

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Arrays, Recursion |
| **Solved on** | 2026-08-11 |
| **How I got there** | Major Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        
        ## First we need to trim the trailing and starting spaces.
        trimmed_s = s.strip()
        sign = 1
        num = 0

        if len(trimmed_s) == 0:
            return 0

        int_min = -(2**31)
        int_max = 2**31 -1

        ## Now we will find the sign of the value and accoringlywe will assign the sign of the value

        if trimmed_s[0] == '-':
            sign = -1
            i = 1
            
        elif trimmed_s[0] == '+':
            i = 1
            
        else:
            i = 0
        
        for i in range( i, len(trimmed_s)):
            if trimmed_s[i].isdigit():
                num = num * 10 + int( trimmed_s[i])
            else:
                break

        if sign == -1:
            num = num * sign
        
        if num < int_min:
            return int_min
        
        elif num > int_max:
            return int_max
        
        else:
            return num

```

- This is the iterative method of the solution.
