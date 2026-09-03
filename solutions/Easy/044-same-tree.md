# 044. Same Tree

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Trees |
| **Solved on** | 2026-04-21 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/same-tree/) |

---

## Problem

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

```
Input: p = [1,2], q = [1,null,2]
Output: false
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

**Constraints:**

* The number of nodes in both trees is in the range `[0, 100]`.
* `-104 <= Node.val <= 104`

## My Notes & Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        return self.same( p,q)

    def same( self, p,q):

        if not p and not q:
            return True
        
        elif (not p and q) or (p and not q):
            return False

        elif p.val == q.val:
            return (self.same( p.left,q.left) and self.same(p.right, q.right))
        
        else:
            return False
```

- Here initially we check if both are totally null then we can just say that the trees are same.

- Then we will call the recursive helper function same(p,q) where we pass both the roots of the trees.

- Then we will first check if both the roots are null which will mean that the tree is same.

- Then we will check if either is null and either is not and then we will be able to retunr False.

- Finally we will check if the val of q and p is same or not, which will obviously mean that they are same because we are also sending in pairs of ( p.left , q.left ) and ( p.right, q.,right )
