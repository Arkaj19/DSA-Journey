# 006. Candy One Pass ( O(1) Space )

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Hard |
| **Topics** | Greedy |
| **Solved on** | 2026-03-12 |
| **How I got there** | Saw Video Soution |
| **Link** | [Problem link](https://leetcode.com/problems/candy/description/) |

---

## Problem

There are `n` children standing in a line.

Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:

* Each child must have **at least** one candy.
* Children with a **higher** rating get more candies than their neighbors.

Return the **minimum** number of candies you need to have to distribute the candies to the children.

**Example 1:**

```
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
```

**Example 2:**

```
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
```

**Constraints:**

* `1 <= n == ratings.length <= 5 * 104`
* `0 <= ratings[i] <= 5 * 104`

## My Notes & Solution

```java
class Solution {
    public int candy(int[] ratings) {
        int candies = 1;
        int up = 0;
        int down = 0;
        int peak = 0;

        for( int i = 1; i<ratings.length; i++)
        {
            int curr = ratings[i];
            int prev = ratings[i - 1];
            if( curr > prev)
            {
                up++;
                peak = up;
                down = 0;
                candies+= up + 1;
            }
            else if( curr < prev)
            {
                down++;
                up = 0;
                candies+= down;

                if( down > peak)
                candies+= 1;
            }
            else
            {
                up = 0;
                down = 0;
                peak = 0;
                candies+= 1;
            }
        }

        return candies;
    }
}
```

#### Candy Problem (LeetCode 135) — Story Notes

- Problem Goal

---

#### Key Insight

- The constraints come from both directions:

- So the distribution depends on increasing and decreasing slopes in the ratings.

---

#### Greedy Idea

Treat ratings as mountain slopes:

```plain text
increasing slope → candies increase
decreasing slope → candies decrease
peak → must satisfy both sides
```

Track:

- up → length of increasing slope

- down → length of decreasing slope

- peak → height of last peak

---

#### Algorithm Flow (O(1) Space)

1. Start with 1 candy for the first child.

1. Traverse the ratings:

---

#### Complexity

```plain text
Time  : O(n)
Space : O(1)
```

---

#### Key Greedy Principle

Instead of storing candies for every child, track lengths of slopes and compute candy contributions dynamically.

---
