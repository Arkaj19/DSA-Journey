# 068. Rotate List

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Linked List |
| **Solved on** | 2026-05-05 |
| **How I got there** | Needed Hint from ChatGpt |
| **Link** | [Problem link](https://leetcode.com/problems/rotate-list/description/?envType=daily-question&envId=2026-05-05) |

---

## Problem

Given the `head` of a linked list, rotate the list to the right by `k` places.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg)

```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg)

```
Input: head = [0,1,2], k = 4
Output: [2,0,1]
```

**Constraints:**

* The number of nodes in the list is in the range `[0, 500]`.
* `-100 <= Node.val <= 100`
* `0 <= k <= 2 * 109`

## My Notes & Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head

        curr = head
        count = 1
        while curr.next:
            curr = curr.next
            count+=1

        k = k % count
        if k == 0:
            return head
        
        curr.next = head

        left = ListNode(-1)
        left.next = head
        right = head

        for i in range( 0, count - k):

            right = right.next
            left = left.next
        
        left.next = None
    
        return right
```

- Here the basic thing is to use modulo because there is no need of repeating all the times.

-
