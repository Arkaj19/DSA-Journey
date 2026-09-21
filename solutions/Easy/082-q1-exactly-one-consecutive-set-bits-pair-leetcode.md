# 082. Q1. Exactly One Consecutive Set Bits Pair©leetcode

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Bit Manipulation, Math, BiWeekly |
| **Solved on** | 2026-06-06 |
| **How I got there** | Minor Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def consecutiveSetBits(self, n: int) -> bool:

        num = n
        final = ""

        while( num > 0):

            digit = num % 2
            final = str(digit) + final
            num = num // 2

        print(final)

        sum = 0
        count = 0

        for i in range(len(final)):
                
            if final[i] == "0":
                sum = 0
                
            if final[i] == "1":
                sum+=1

            if sum >= 2:
                count+=1

        if count == 1:
            return True

        else:
            return False
```
