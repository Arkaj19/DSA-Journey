# 026. Topological Sort

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Graphs |
| **Solved on** | 2026-04-14 |
| **How I got there** | Saw Video Soution |
| **Link** | [Problem link](https://takeuforward.org/plus/dsa/problems/topological-sort-or-kahns-algorithm) |

---

## Problem

_Couldn't auto-fetch the statement (paid-only question, or the source page changed). See the [original link](https://takeuforward.org/plus/dsa/problems/topological-sort-or-kahns-algorithm)._

## My Notes & Solution

```python
class Solution:
    def topoSort(self, V, adj):

        visited = set()
        ans = []

        for i in range(V):
            if i not in visited:
                self.topo_sort(i, visited, ans, adj)

        return ans[::-1]

            

    def topo_sort(self,curr,visited,ans,adj):
        visited.add(curr)

        for neighbour in adj[curr]:
            if neighbour not in visited:
                self.topo_sort(neighbour,visited,ans,adj)
            
        ans.append(curr)
```

- Here we are using the DFS methodology to solve the problem here.

- Here the answer that is returned to us is in a reverse order. 

- Hence we need to reverse at the end of the
