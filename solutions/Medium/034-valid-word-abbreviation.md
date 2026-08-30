# 034. Valid Word Abbreviation

| | |
|---|---|
| **Platform** | NeetCode |
| **Difficulty** | Medium |
| **Topics** | Strings, Two Pointers |
| **Solved on** | 2026-04-17 |
| **How I got there** | Major Thinking required |
| **Link** | [Problem link](https://neetcode.io/problems/valid-word-abbreviation/question) |

---

## Problem

_Couldn't auto-fetch the statement (paid-only question, or the source page changed). See the [original link](https://neetcode.io/problems/valid-word-abbreviation/question)._

## My Notes & Solution

```python
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        if abbr == word:
            return True

        num = 0
        i = 0
        j = 0

        while i< len(word) and j < len(abbr):
            
            if word[i] == abbr[j]:
                i+=1
                j+=1
            
            elif abbr[j].isdigit():
                if abbr[j] == '0' and num == 0:
                    return False
                num = num * 10 + int(abbr[j])
                j+=1

            
            elif abbr[j].isalpha():
                print(f'i value is -> {i}')
                i = i + num
                print(f'i value is -> {i} and the num value was -> { num}')
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                num = 0
                j+=1
                i+=1


        print( f'i is -> {i} and j is -> {j}')

        if num != 0:
            i = i+num
            if i > len(word):
                return False

        # if i != len(word) and j != len(abbr):
        #     return False
        
        # return  i == len(word) and j == len(abbr)
        return True
    

```
