# 043. Maximum Depth of Binary Tree

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Trees |
| **Solved on** | 2026-04-21 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/) |

---

## Problem

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2:**

```
Input: root = [1,null,2]
Output: 2
```

**Constraints:**

* The number of nodes in the tree is in the range `[0, 104]`.
* `-100 <= Node.val <= 100`

## My Notes & Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        return self.dfs( root)

    def dfs(self,root):

        if not root:
            return 0
        
        left = self.dfs( root.left)
        right = self.dfs( root.right)
        return max(left,right) + 1
```

- Here everytime the root is null we return back 0.

- Else we explore the left and right

- Now we add the 1 at the max of the left and right because here we also have been mentioned that the number of node defines the depth of the tree.

```python
print(”arka”)
```
