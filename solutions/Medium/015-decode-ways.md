# 015. Decode Ways


| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | DP |
| **Solved on** | 2026-04-01 |
| **How I got there** | Saw Video Soution |
| **Link** | [Problem link](https://leetcode.com/problems/decode-ways/) |

---

## Problem

You have intercepted a secret message encoded as a string of numbers. The message is **decoded** via the following mapping:

`"1" -> 'A'  
"2" -> 'B'  
...  
"25" -> 'Y'  
"26" -> 'Z'`

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes (`"2"` and `"5"` vs `"25"`).

For example, `"11106"` can be decoded into:

* `"AAJF"` with the grouping `(1, 1, 10, 6)`
* `"KJF"` with the grouping `(11, 10, 6)`
* The grouping `(1, 11, 06)` is invalid because `"06"` is not a valid code (only `"6"` is valid).

Note: there may be strings that are impossible to decode.  
  
Given a string s containing only digits, return the **number of ways** to **decode** it. If the entire string cannot be decoded in any valid way, return `0`.

The test cases are generated so that the answer fits in a **32-bit** integer.

**Example 1:**

**Input:** s = "12"

**Output:** 2

**Explanation:**

"12" could be decoded as "AB" (1 2) or "L" (12).

**Example 2:**

**Input:** s = "226"

**Output:** 3

**Explanation:**

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

**Example 3:**

**Input:** s = "06"

**Output:** 0

**Explanation:**

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

**Constraints:**

* `1 <= s.length <= 100`
* `s` contains only digits and may contain leading zero(s).

## My Notes & Solution

```python
class Solution:

    count = 0
    def numDecodings(self, s: str) -> int:

        self.count = 0
        self.solve( s, "")
        return self.count

    def solve( self, s, last):

        if len(s) == 0:
            self.count+=1
            return

        ## tAKE 1 
        one = s[-1]
        if self.is_valid(one):
            self.solve(s[:-1],one)

        ## tAKE 2 
        if len(s) >= 2:
            two = s[-2:]
            if self.is_valid(two):
                self.solve(s[:-2],two)
                
    def is_valid( self, s):

        # num = int(s)

        if len(s) == 1:
            if int(s) >= 1 and int(s) <= 9:
                return True

        elif len(s) == 2:
            if int(s) >= 10 and int(s) <= 26:
                return True

        return False      
        
```

Recursive Solution:

- we have 2 options : Either take 1 element from last or take 2 elements.

- to send the last 2 characters s[-2:] because s[-2] send s the 2nd last charcter.

- Don't count for each character

-  count increases after we have reached the end

- for helper function:

DP ( Memoization )

→ Self is the representation of the current instance of the class.
→ Without self, Python won’t know where ways is defined.
→ We initialize the dp with a self because it allows us to be 


```python
class Solution:
    def numDecodings(self, s: str) -> int:
        self.dp = {}
        return self.ways(s)
    
    def ways(self,rems):

        if rems == '':
            return 1
        
        if rems in self.d:
            return self.dp[rems]

        count = 0
        
        one = rems[-1]
        if one != '0':
            count+= self.ways(rems[:-1])
        
        if len(rems) >=2:
            two = rems[-2:]
            if int(two) >= 10 and int(two) <= 26:
                count += self.ways(rems[:-2])

        self.dp[rems] = count
        return count
```

→ We are just storing the values hence we dont need a 2d dp and a 1d dp is enough to do the work.

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.dp = {}
        return self.ways(s, wordDict)
    
    def ways( self,rems,wordDict):
        if rems == '':
            return True
        
        if rems in self.dp:
            return self.dp[rems]
        
        res = False
        
        for i in range(len(rems)):
            substr = rems[0:i+1]
            if substr in wordDict and self.ways(rems[i+1:],wordDict):
                res = True
        self.dp[rems] = res

        return self.dp[rems]
```
