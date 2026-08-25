# 024. All paths from source to target

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Graphs |
| **Solved on** | 2026-04-13 |
| **How I got there** | Saw Video Soution |
| **Link** | [Problem link](https://leetcode.com/problems/all-paths-from-source-to-target/description/) |

---

## Problem

Given a directed acyclic graph (**DAG**) of `n` nodes labeled from `0` to `n - 1`, find all possible paths from node `0` to node `n - 1` and return them in **any order**.

The graph is given as follows: `graph[i]` is a list of all nodes you can visit from node `i` (i.e., there is a directed edge from node `i` to node `graph[i][j]`).

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg)

```
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/28/all_2.jpg)

```
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```

**Constraints:**

* `n == graph.length`
* `2 <= n <= 15`
* `0 <= graph[i][j] < n`
* `graph[i][j] != i` (i.e., there will be no self-loops).
* All the elements of `graph[i]` are **unique**.
* The input graph is **guaranteed** to be a **DAG**.

## My Notes & Solution

```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Here we are already given the adjacency list
        
        allPaths = []
        end = len(graph) - 1
        path = [0]
        self.find_paths(0,graph,allPaths,end,path)
        return allPaths

    def find_paths( self,curr,graph,allPaths,end,path):

        if curr == end:
            allPaths.append(path.copy())
            return
        
        for neighbour in graph[curr]:
            
            # First push to allPaths
            path.append(neighbour)
            # Calling the function
            self.find_paths(neighbour,graph,allPaths,end,path)
            # Backtrack again
            path.pop()
        
```

- Here we are essentially using the recursive dfs methodology.

- Our loop continues till it reaches the end node.

- We implement backtracking here.

- Here at first we append the neighbour to the path.

- Then we call the recursive dfs function again.

- Then we pop the element from the path list.

- In this way it goes on and on.

- Once we get the destination that refers to a valid path we have found and hence we add it to the allPaths but we add a copy of it as it can alter the main variable.
