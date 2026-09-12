# 064. Maximum Path Score in a Grid

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Grid, DP |
| **Solved on** | 2026-04-27 |
| **How I got there** | — |
| **Link** | [Problem link](https://leetcode.com/problems/maximum-path-score-in-a-grid/) |

---

## Problem

You are given an `m x n` grid where each cell contains one of the values 0, 1, or 2. You are also given an integer `k`.

You start from the top-left corner `(0, 0)` and want to reach the bottom-right corner `(m - 1, n - 1)` by moving only **right** or **down**.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

* 0: adds 0 to your score and costs 0.
* 1: adds 1 to your score and costs 1.
* 2: adds 2 to your score and costs 1. ​​​​​​​

Return the **maximum** score achievable without exceeding a total cost of `k`, or -1 if no valid path exists.

**Note:** If you reach the last cell but the total cost exceeds `k`, the path is invalid.

**Example 1:**

**Input:** grid = [[0, 1],[2, 0]], k = 1

**Output:** 2

**Explanation:**​​​​​​​

The optimal path is:

| Cell | grid[i][j] | Score | Total  Score | Cost | Total  Cost |
| --- | --- | --- | --- | --- | --- |
| (0, 0) | 0 | 0 | 0 | 0 | 0 |
| (1, 0) | 2 | 2 | 2 | 1 | 1 |
| (1, 1) | 0 | 0 | 2 | 0 | 1 |

Thus, the maximum possible score is 2.

**Example 2:**

**Input:** grid = [[0, 1],[1, 2]], k = 1

**Output:** -1

**Explanation:**

There is no path that reaches cell `(1, 1)`​​​​​​​ without exceeding cost k. Thus, the answer is -1.

**Constraints:**

* `1 <= m, n <= 200`
* `0 <= k <= 103​​​​​​​`
* `​​​​​​​grid[0][0] == 0`
* `0 <= grid[i][j] <= 2`

## My Notes & Solution

- This is just the Recursion approach of the problem

```python
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:

        score = 0
        cost = 0
        result = self.find_path( grid, k, 0,0,score,cost)

        if result == float('-inf'):
            return -1
        else:
            return result


    def find_path( self, grid, k, row, col,score,cost):
    
        if row >= len(grid) or col >= len( grid[0]):
            return float('-inf')
        
        if grid[row][col] == 0:
            cost+=0
            score+=0
        
        elif grid[row][col] == 1:
            cost+=1
            score+=1
        
        elif grid[row][col] == 2:
            cost+=1
            score+=2
        
        if cost > k:
            return float('-inf')
        
        if row == len(grid) - 1 and col == len( grid[0]) - 1 and cost <= k:
            return score
        
        return max(self.find_path( grid, k, row+1, col, score, cost ), self.find_path( grid, k, row, col+1, score, cost))
        

```

- This is the DP implementation of the Recursive approach.

```python
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:

        score = 0
        cost = 0
        self.dp = {}
        result = self.find_path(grid, k, 0,0,cost)

        if result == float('-inf'):
            return -1
        else:
            return result


    def find_path( self, grid, k, row, col,cost):
            
        if row >= len(grid) or col >= len(grid[0]):
            return float('-inf')

        new_cost=cost

        if grid[row][col]!=0:
            new_cost+=1

        if new_cost>k:
            return float("-inf")

        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return grid[row][col]

        if (row,col,cost) in self.dp:
            return self.dp[(row,col,cost)]
        
        go_right=grid[row][col]+self.find_path(grid,k,row,col+1,new_cost)
        go_down=grid[row][col]+self.find_path(grid,k,row+1,col,new_cost)
        
        self.dp[(row,col,cost)]=max(go_right,go_down)

        return self.dp[(row,col,cost)]
```

-
