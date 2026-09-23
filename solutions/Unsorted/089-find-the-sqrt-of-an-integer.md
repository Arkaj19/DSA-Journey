# 089. Find the sqrt of an integer

| | |
|---|---|
| **Platform** | Other |
| **Difficulty** | Unsorted |
| **Topics** | — |
| **Solved on** | 2026-07-06 |
| **How I got there** | Saw Video Soution |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

Brute Force

```python
class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0
            
        ans = 1

        for i in range( 1, x + 1):

            if i * i <= x:
                ans = i
            else:
                break
        
        return ans
```

Optimized Version using Binary Search

- Always remember if there is a condition such that till one point we have a answer and after a certain point we don’t have one then we can apply BS.

- Now as we can see here if the x is 28 then in first time the mid is 15 and 15*15 is heavily greater than 28.

- Hence we can say one thing and that is all values above 15 will be of no use as all will be greater.

- Then we should shrink the high in this case.

- But in the opposite case at one point we reach 3 and 3 * 3 ≤ 28 hence it might be an answer so we make 

```python
ans = mid
low = mid + 1

## This is because we might be in the answer zone but going below 3 i.e. to 1,2 wont do us any good.

## That is because 2*2 and 1*1 will obviously be smaller so hence we make the low as mid + 1.

## In this way we are also keeping track of the last possible number and also searching for a number more closer to the answer.
```
