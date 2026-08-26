# 025. Detect cycle in undirected Connected Graph

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Graphs |
| **Solved on** | 2026-04-13 |
| **How I got there** | — |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

- For this question we cannot just focus on basic DFS such that when the same node is encountered it is said to be as having a cycle.

- But for this we will have to keep track of the parents of each node.

- This is because if the node doesnt have a parent till now that means it is a standalone path but for instance if it has a parent earlier and again when we will reach it then we will see that there are 2 parent nodes for a single node which is not possible

- This shows that it has formed a cycle about that node.

```python
class Solution:
	def isCycle(self, V, edges):
		#Code here
		
		ad = {}
		visited = set()
		
		for u,v in edges:
		    if u not in ad:
		        ad[u] = []
		       
		    if v not in ad:
		        ad[v] = []
		        
		    ad[u].append(v)
		    ad[v].append(u)
		
		
	    
	    return self.dfs_cycle(0,ad,visited,-1)
	    
	
	def dfs_cycle(self,curr,ad,visited,parent):
	    
	    visited.add(curr)
	    
	    for neighbour in ad[curr]:
	        if neighbour not in visited:
	            if self.dfs_cycle(neighbour,ad,visited,curr):
	                return True
            elif neighbour != parent:
                return True
            
	    return False
```

- Considering that there are no disconnected graphs this is the solution for us which follows the recursive DFS algorithm to find the elements.
