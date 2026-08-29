# 033. Anagram Palindrome

| | |
|---|---|
| **Platform** | GFG |
| **Difficulty** | Easy |
| **Topics** | Arrays |
| **Solved on** | 2026-04-17 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://www.geeksforgeeks.org/problems/anagram-palindrome4720/1) |

---

## Problem

_Couldn't auto-fetch the statement (paid-only question, or the source page changed). See the [original link](https://www.geeksforgeeks.org/problems/anagram-palindrome4720/1)._

## My Notes & Solution

```python
class Solution:
    def canFormPalindrome(self, s):
        # code here
        
        count = 0
        cdict = {}
        
        
        for ch in s:
            if ch not in cdict or cdict[ch] == 0:
                cdict[ch] = 1
            else:
                cdict[ch] = cdict[ch] - 1
            
            # print(cdict)
        
        for v in cdict.values():
            if v % 2 != 0:
                count+=1
        
        if count > 1:
            return False
        else:
            return True
```

- Here basically we are at all times storing the number of occurrences in a dict and then when we get the same element again then we just basically deduct that number.

- Here then at the end we will loop over the dict and access the values and check if the odd is thet or not .

- If any odd number is found and the occurence of such an alphjabet is only 1 times then ok but if it goes more than 1 then it can never be Palindrome.
