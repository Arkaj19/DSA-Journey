# 045. Detect Capital 

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Strings |
| **Solved on** | 2026-04-22 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/detect-capital/) |

---

## Problem

We define the usage of capitals in a word to be right when one of the following cases holds:

* All letters in this word are capitals, like `"USA"`.
* All letters in this word are not capitals, like `"leetcode"`.
* Only the first letter in this word is capital, like `"Google"`.

Given a string `word`, return `true` if the usage of capitals in it is right.

**Example 1:**

```
Input: word = "USA"
Output: true
```

**Example 2:**

```
Input: word = "FlaG"
Output: false
```

**Constraints:**

* `1 <= word.length <= 100`
* `word` consists of lowercase and uppercase English letters.

## My Notes & Solution

```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        n = len(word)
        capital_count = 0

        ## This tackles the case of word starting with 
        if ord(word[0]) >= 65 and ord(word[0]) <= 90:
            capital_count+=1
            for i in range(1,n):
                if ord(word[i]) >= 65 and ord(word[i]) <= 90:
                    capital_count+=1
            
            if capital_count < n and capital_count > 1:
                return False
            
        else:
            for i in range( 1,n):
                if ord(word[i]) >= 65 and ord(word[i]) <= 90:
                    return False
        
        return True
```

- Here the first level of divergence comes when we check whether the first character is capital or not.

- If the first letter is capital then we know that the rest of the letter can be either capital or the rest of the letter has to be small.

- Again on the opposite side if we check that the first letter is short character then the other letters must be small and the even if a single capital letter comes then we will have to return False then and there.
