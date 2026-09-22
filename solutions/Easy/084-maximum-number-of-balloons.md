# 084. Maximum Number of Balloons

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Frequency Array |
| **Solved on** | 2026-06-26 |
| **How I got there** | Minor Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        min_count = float('inf')
        n = len(text)
        freq = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        
        for i,char in enumerate(text):

            if char in freq:
                freq[char]+=1

        for i in freq:
            if i == 'b':
                count_b =  freq[i] // 1
                min_count = min(count_b,min_count)
            
            elif i == 'a':
                count_a =  freq[i] // 1
                min_count = min(count_a,min_count)
            
            elif i == 'l':
                count_l =  freq[i] // 2
                min_count = min(count_l,min_count)
            
            elif i == 'o':
                count_o =  freq[i] // 2
                min_count = min(count_o,min_count)
            
            else:
                count_n =  freq[i] // 1
                min_count = min(count_n,min_count)
        
        return min_count
```

- Here the basic thing is that I dont need to keep the count of the word balloon but we have to create freq array for future use.

- Then we will find the freq of each character of the text which falls within the letters of the word Balloon.

- then we are going to divide those with the respective freq of each letter as it should be to create a proper word.

- Finally the minimum of them all will be giving us our required answer.

- This is because the minimum means that many words can be formed at the very least.
