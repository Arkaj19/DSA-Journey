# 112. Count good numbers

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Recursion, binary Exponentiation |
| **Solved on** | 2026-08-16 |
| **How I got there** | Saw Video Soution, Major Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

- Number of even indices : - ( n+1) / 2

- Number of odd indices :- ( n/2 )

- Here it is a basic probability based problem as we can see that for even indices we have 5 nuimbers at those postiions and for odd we can place at most 4 prime numbers.

- Now if we were to associate the count of numbers possible associated to the count of positions it will give us the total number.

```python
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        MOD = 10**9 + 7
        result = self.solve(0,n)

        return result % MOD

    def solve(self, index, n):

        if index == n:
            return 1

        if index % 2 == 0:
            return 5 * self.solve( index + 1, n)

        else:
            return 4 * self.solve( index + 1, n)
```
