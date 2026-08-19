# 005. Candy Two Pass ( O(n) Space )

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Hard |
| **Topics** | Greedy |
| **Solved on** | 2026-03-12 |
| **How I got there** | Needed Hint from ChatGpt |
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

#### Candy Problem – Story Notes (Greedy Two-Pass Approach)

- Problem Goal

---

- Key Observation

---

- Step 1 – Left → Right Pass

---

- Step 2 – Right → Left Pass

---

- Step 3 – Combine Both Constraints

---

- Final Step

---

- Complexity

---

- Core Greedy Insight

```java
class Solution {
    public int candy(int[] ratings) {

        int n = ratings.length;
        int candies_left[] = new int[n];
        int candies_right[] = new int[n];
        int candies[] = new int[n];
        Arrays.fill(candies_left, 1);  // 1st Condition: Each child gets a candy for sure
        Arrays.fill(candies_right, 1);  // 1st Condition: Each child gets a candy for sure

        // Flowing left to right
        for( int i = 1; i<n; i++)
        {
            int curr_rating = ratings[i];
            if( curr_rating > ratings[i -1])
            {
                candies_left[i] = candies_left[i-1] + 1;
            }
        }

        // Now flowing from right to left
        for( int i = n-2; i>=0; i--)
        {
            int curr_rating = ratings[i];
            if( curr_rating > ratings[i + 1])
            {
                candies_right[i] = candies_right[i+1] + 1;
            }
        }

        int sum = 0;
        for( int i = 0; i<n; i++)
        {
            candies[i] = Math.max(candies_left[i], candies_right[i]);
            sum+=candies[i];
        }
        return sum;
    }
}
```
