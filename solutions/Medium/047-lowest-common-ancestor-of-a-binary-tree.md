# 047. Lowest Common Ancestor Of a Binary Tree

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Trees |
| **Solved on** | 2026-04-22 |
| **How I got there** | Saw Video Soution |
| **Link** | [Problem link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) |

---

## Problem

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

**Example 3:**

```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

**Constraints:**

* The number of nodes in the tree is in the range `[2, 105]`.
* `-109 <= Node.val <= 109`
* All `Node.val` are **unique**.
* `p != q`
* `p` and `q` will exist in the tree.

## My Notes & Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        arr_p = []
        arr_q = []
        self.find_lca( root, p, arr_p )
        self.find_lca( root, q, arr_q )

        n = min( len(arr_p), len(arr_q))

        for i in range(n):
            if arr_p[i] == arr_q[i]:
                match = arr_p[i]
        
        return match


    def find_lca( self, curr, target, arr):
        
        if not curr:
            return False
        
        arr.append( curr )

        if curr == target:
            return True

        left = self.find_lca(curr.left, target, arr)
        right = self.find_lca( curr.right, target, arr)

        if left or right:
            return True

        arr.pop()
        return False
```

- Here the solution as made here is a basic brute force approach as we are creating arrays of paths.

- Then we will calling our helper recurscive function which does the following:

### Optimal Approach:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        return self.dfs_lca( root,p,q)

    def dfs_lca( self,root,p,q):

        if not root:
            return False
        
        if root.val == p.val or root.val == q.val:
            return root
        
        right = self.dfs_lca(root.right, p,q)
        left = self.dfs_lca(root.left, p,q)

        if right and not left:
            return right
        
        if left and not right:
            return left

        if right and left:
            return root
        
        return None

```

- Here the main concept is to treat the problem as a game. 

- When we find either we return the target node above.

- If we have been able to find both the targets then we will return the current node. 

- This is like 2 people are coming with batons running to an intersection point. There is a main standing in the intersection point.

- As soon as both came to him he started running above and told everyone that “mere karan arjun agaye hai hai”
