# 049. Palindrome Linked List

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Linked List |
| **Solved on** | 2026-04-22 |
| **How I got there** | Could solve it instantly |
| **Link** | [Problem link](https://leetcode.com/problems/palindrome-linked-list/) |

---

## Problem

Given the `head` of a singly linked list, return `true` *if it is a* *palindrome* *or* `false` *otherwise*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)

```
Input: head = [1,2,2,1]
Output: true
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg)

```
Input: head = [1,2]
Output: false
```

**Constraints:**

* The number of nodes in the list is in the range `[1, 105]`.
* `0 <= Node.val <= 9`

**Follow up:** Could you do it in `O(n)` time and `O(1)` space?

## My Notes & Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        arr = []

        while curr:
            arr.append( curr.val)
            curr = curr.next

        j = len(arr) - 1
        i = 0

        while i <j:
            if arr[i] == arr[j]:
                i+=1
                j-=1
                continue
            else:
                return False


        return True

```

- This is the naive approach where we are using an array to store the elements of the array as we traverse forward.

- Here it consumes O(n) TC which is good but has O(n) SC which is optimizable

Optimized for Space Complexity of O(1)

-
