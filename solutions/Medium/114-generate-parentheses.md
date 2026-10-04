# 114. Generate Parentheses

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Recursion |
| **Solved on** | 2026-08-18 |
| **How I got there** | Major Thinking required |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    res = []
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.res = []
        self.solve( "", n)
        return self.res

    def solve( self, s, n):

        if len(s) == 2 * n:

            if self.isvalid(s):
                self.res.append(s)
            return 

        self.solve( s + "(", n)
        self.solve( s + ")", n)
    
    def isvalid( self, s ):

        st = []
        c = 0

        for i in range( len(s)):

            if s[i] == "(":
                c+=1
            else:
                c-=1

            if c < 0:
                return False
        
        if c == 0:
            return True
        else:
            return False
```

- isValid() → use counter to check the number of “(” and “)”

- +1 for every “(”

- -1 for every “)”

- there will be 3 cases:

Solve()

- Base cd. : cHECK WHETHER LENGTH OF STRING HAS reached 2 *n  or not. THEN CALL isvalid().

- then we have 2 options: 

- No backtracking code required explicitly
