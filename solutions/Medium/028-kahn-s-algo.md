# 028. Kahn’s Algo

| | |
|---|---|
| **Platform** | GFG |
| **Difficulty** | Medium |
| **Topics** | Graphs |
| **Solved on** | 2026-04-15 |
| **How I got there** | — |
| **Link** | [Problem link](https://takeuforward.org/plus/dsa/problems/topological-sort-or-kahns-algorithm) |

---

## Problem

_Couldn't auto-fetch the statement (paid-only question, or the source page changed). See the [original link](https://takeuforward.org/plus/dsa/problems/topological-sort-or-kahns-algorithm)._

## My Notes & Solution

```python
from collections import deque
class Solution:
    def topoSort(self, V, adj):

        ## Initially we create an indegree array and initialize all the values with 0
        indegree = [0] * V 

        ## We will access all the indexes of the graph
        for i in range(V):
            ## Here we will check we will go through the neighbours of the nodes to check the occurence of them for indegree array
            for j in adj[i]:
                indegree[j]+=1

        queue = deque()

        for i in range(V):
            ## If indegree of any node is 0 then we will add it in the queue
            if indegree[i] == 0:
                queue.append(i)

        ans = []
        
        ## While the queue is not empty we will take an element out and search for its neigbours
        while(queue):

            ## Extracting the current node
            curr = queue.popleft()
            ans.append(curr)
            ## Exploring the current node and then we will reduce its indegree by 1
            for neighbour in adj[curr]:
                indegree[neighbour]-=1
                if (indegree[neighbour] == 0):
                    queue.append(neighbour)

        return ans
```

### Steps:- 

- In case of Kahn’s algo the indegree of each node matters a lot.

- So first of all we will create a indegree array which will contain the indegree values of all the elements.

- Indegree means the number of inward edges of a node.

- Now as we know that we always use a queue in case of the BFS and at the same time we will also keep a visited array.

- At first we will put the elements having the indegree as 0 in the queue.

- Now we will pop one from the queue and start processing it i.e. to access its neighbours and check their indegree and each time we will reduce the indegree by 1

- Then as soon as the indegree of the neighbours become 0 we will add them in the queue. 

- Then we will access them and again add them in the visited.
