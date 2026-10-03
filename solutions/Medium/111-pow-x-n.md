# 111. pow(x,n)

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Recursion |
| **Solved on** | 2026-08-11 |
| **How I got there** | Saw Video Soution, Major Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        return self.calculate( x,n)

    def calculate (self, x, n):

        if n == 0:
            return 1
        
        if n > 0:
            return x * self.calculate(x ,(n-1))

        else:
            return (1/x) * self.calculate(x , (n+1) )
```

- This is the code for aam zindagi.

- Here we are just doing a basic multiplication only i.e. x * x * x *. … and this can go on for a lot and this leads to TLE.

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        return self.calculate( x,n)

    def calculate (self, x, n):

        if n == 0:
            return 1
        
        if n < 0:
            x = 1/x
            n = -n

        if n % 2 == 0:

            return self.calculate( x * x, n//2)
        z
        else:
            return ( x * self.calculate( x * x , n//2 ))

```

### Pow(x, n) — Quick Revision

- If the exponent is 0, return 1

- If the exponent is negative

- Check whether the exponent is even or odd

- If the exponent is even

- If the exponent is odd

- Keep repeating

```plain text
✓ n < 0, not x < 0
✓ n % 2, not x % 2
✓ n // 2, not n / 2
✓ Base case: n == 0
```
