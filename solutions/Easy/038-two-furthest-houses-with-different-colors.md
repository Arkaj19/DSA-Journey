# 038. Two Furthest Houses With Different Colors

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Arrays, Greedy, Two Pointers |
| **Solved on** | 2026-04-20 |
| **How I got there** | Needed Hint from ChatGpt |
| **Link** | [Problem link](https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/?envType=daily-question&envId=2026-04-20) |

---

## Problem

There are `n` houses evenly lined up on the street, and each house is beautifully painted. You are given a **0-indexed** integer array `colors` of length `n`, where `colors[i]` represents the color of the `ith` house.

Return *the **maximum** distance between **two** houses with **different** colors*.

The distance between the `ith` and `jth` houses is `abs(i - j)`, where `abs(x)` is the **absolute value** of `x`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/10/31/eg1.png)

```
Input: colors = [1,1,1,6,1,1,1]
Output: 3
Explanation: In the above image, color 1 is blue, and color 6 is red.
The furthest two houses with different colors are house 0 and house 3.
House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
Note that houses 3 and 6 can also produce the optimal answer.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/10/31/eg2.png)

```
Input: colors = [1,8,3,8,3]
Output: 4
Explanation: In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
The furthest two houses with different colors are house 0 and house 4.
House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.
```

**Example 3:**

```
Input: colors = [0,1]
Output: 1
Explanation: The furthest two houses with different colors are house 0 and house 1.
House 0 has color 0, and house 1 has color 1. The distance between them is abs(0 - 1) = 1.
```

**Constraints:**

* `n == colors.length`
* `2 <= n <= 100`
* `0 <= colors[i] <= 100`
* Test data are generated such that **at least** two houses have different colors.

## My Notes & Solution

```python
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        if len(colors) == 1:
            return 0
        
        n = len(colors)

        if colors[0] != colors[n-1]:
            return n - 1

        i = 0
        j = n - 1

        while colors[j] == colors[0]:
            j-=1

        while colors[i] == colors[n-1]:
            i+=1

        return max( j, abs(n - i - 1))
```

- Here the question is quite straight forward in terms that if we need to get the farthest distance then it should be checked from the either end points only.

- So once we loop from the 0th index to the n-1th point.

- Then we loop again from the n-1th point to the 0th point.

- From here we get the two points where the first difference is encountered.

- One from the right and another from the left.

- Now the one from the right is ok because that is j which is already from the 0th index.

- But for the one from left side we need to minus it from the n.

- Such that we get the difference from the beginning at that point.

Finally we return the max out of these points.
