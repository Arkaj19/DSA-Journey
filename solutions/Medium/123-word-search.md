# 123. Word search

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Recursion |
| **Solved on** | 2026-08-29 |
| **How I got there** | Major Thinking required, Saw Video Soution |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        visited = []

        for i in range( rows):

            row = []
            for j in range ( cols):
                row.append(-1)

            visited.append(row)

        def check( r,c,i):

            if i == len(word):
                return True

            if r < 0 or r >= len(board):
                return False
            
            if c < 0 or c >= len(board[0]):
                return False

            if visited[r][c] == 1:
                return False
            
            if visited[r][c] != 1 and board[r][c] != word[i]:
                return False
            
            visited[r][c] = 1
            res = (check(r+1,c,i+1) or 
                   check(r,c+1,i+1) or
                   check(r-1,c,i+1) or
                   check(r,c-1,i+1))

            visited[r][c] = -1  
            return res
        
        for i in range(rows):
            for j in range(cols):
                if check(i,j,0):
                    return True

        return False
```

- There are 4 base conditions:
