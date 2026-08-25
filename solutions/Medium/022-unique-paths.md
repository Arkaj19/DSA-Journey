# 022. unique paths

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | DP |
| **Solved on** | 2026-04-07 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/unique-paths/description/) |

---

## Problem

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The test cases are generated so that the answer will be less than or equal to `2 * 109`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

```
Input: m = 3, n = 7
Output: 28
```

**Example 2:**

```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

**Constraints:**

* `1 <= m, n <= 100`

## My Notes & Solution

Here this is very simple: 

- The dp will have the keys as (rows,cols) for each.

-  The recursive call is to be in this way that the current element is formed from the (rows+1,cols) + (rows,cols+1) for each point.

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.dp = {}
        return self.ways( 0,0,m,n)

    def ways( self,rows:int,cols:int, m,n):
        if rows == m - 1 and cols == n - 1:
            return 1

        if rows >= m or cols >=n:
            return 0
        
        if (rows,cols) in self.dp:
            return self.dp[(rows,cols)]
        
        self.dp[(rows,cols)] =(self.ways(rows+1,cols,m,n) + self.ways(rows, cols+1,m,n))
        return self.dp[(rows,cols)]
```
