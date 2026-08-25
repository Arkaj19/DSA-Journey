# 023. Find if Path Exists in Graph

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Graphs |
| **Solved on** | 2026-04-11 |
| **How I got there** | — |
| **Link** | [Problem link](https://leetcode.com/problems/find-if-path-exists-in-graph/description/) |

---

## Problem

There is a **bi-directional** graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (**inclusive**). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [ui, vi]` denotes a bi-directional edge between vertex `ui` and vertex `vi`. Every vertex pair is connected by **at most one** edge, and no vertex has an edge to itself.

You want to determine if there is a **valid path** that exists from vertex `source` to vertex `destination`.

Given `edges` and the integers `n`, `source`, and `destination`, return `true` *if there is a **valid path** from* `source` *to* `destination`*, or* `false` *otherwise**.*

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/08/14/validpath-ex1.png)

```
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/08/14/validpath-ex2.png)

```
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
```

**Constraints:**

* `1 <= n <= 2 * 105`
* `0 <= edges.length <= 2 * 105`
* `edges[i].length == 2`
* `0 <= ui, vi <= n - 1`
* `ui != vi`
* `0 <= source, destination <= n - 1`
* There are no duplicate edges.
* There are no self edges.

## My Notes & Solution

## BFS Approach ( USING QUEUE )

```python
from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #Creating an adjacency list here 
        mp = {}

        for a,b in edges:
            if a not in mp:
                mp[a] = []
            
            if b not in mp:
                mp[b] = []

            mp[a].append(b)
            mp[b].append(a)

        queue = deque([source])
        visited = set([source])

        while(queue):
            curr = queue.popleft()

            if curr == destination: ## Checking happens here
                return True
            
            ## Here we are just adding to the visited and the queue
            for neighbour in mp[curr]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return False           


```

#### Steps

1. First we need to create an adjacency list because what is provided to us is a 2D array .

1. We have used a dict named “mp” as the adjacency list.

1. Then every time we traverse over the elements of the 2d array we create the connection like this :

```python
-->>> This is an Adjacency list where each element is linked to each other such that 
-->>> mp[a] = b and mp[b] = a


{
	0: [1, 2], 
	1: [0], 
	2: [0], 
	3: [5, 4], 
	5: [3, 4], 
	4: [5, 3]
}
```

1. Then we will initialise the queue and the visited set.

1. We use set because we are told that there are no duplicates there.

1. Now the first element is added to the queue and the visited set.

1. Now we run a while condition unless the queue is empty.

1. Everytime we take the curr element and check if its the destination value . if yes we return True.

1. Else we go over the neighbours of it .

1. Hence the main checking is happening here:

```python
if curr == destination: ## Checking happens here
	  return True
```

1. Finally if we never reach the destination then we return False.

## DFS Approach ( Using Stack )

```python
from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #Creating an adjacency list here 
        mp = {}

        for a,b in edges:
            if a not in mp:
                mp[a] = []
            
            if b not in mp:
                mp[b] = []

            mp[a].append(b)
            mp[b].append(a)

        print(mp)

        stack = [source]
        visited = set([source])

        while(stack):
            curr = stack.pop()

            if curr == destination: ## Checking happens here
                return True
            
            ## Here we are just adding to the visited and the queue
            for neighbour in mp[curr]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

        return False           

```
