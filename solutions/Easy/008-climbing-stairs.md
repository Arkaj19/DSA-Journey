# 008. Climbing Stairs

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | DP |
| **Solved on** | 2026-03-22 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/climbing-stairs/description/) |

---

## Problem

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example 1:**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

**Constraints:**

* `1 <= n <= 45`

## My Notes & Solution

### 1. Memoization 

Here the base condition is n ≤ 2 because if our step count is 2 :

→ Then we can either reach that by 1+1 step , OR

→ We can reach by direct 2 steps 

Hence, there are only 2 possibilities hence in case of n ≤ 2 we go for the value of n only.

This question is same as that of the fibonacci series only because here also a particular step is formed from the other two steps.

```java
class Solution {
    private Map<Integer,Integer>mp = new HashMap<>();
    public int climbStairs(int n) {
        if( n <= 2)
            return n; // this is because if our n is 2 that can be reached by wither 1 step twice or direct 2 steps so there are only 2 choices hence our base condition check for <= 2

        if( !mp.containsKey(n))
        {
            mp.put(n, (climbStairs(n-1) + climbStairs(n - 2)));
        }
        return mp.get(n);
    }
}
```

### 2. Tabulation

⇒ Here the thing is first we need to be able to handle the edge cases that is if n is 1 and 2 resepectively.
⇒ Then we need to start the loop from 3 as because for the first 2 we already know the result and we need to check the combinations starting from 3.

```javascript
class Solution {
    public int climbStairs(int n) {
        int step1 = 1;
        int step2 = 2;

        if( n == 1)
        return 1;
        if( n == 2)
        return 2;

        for( int i = 3; i<=n; i++)
        {
            int curr = step1 + step2;
            step1 = step2;
            step2 = curr;
        }
        return step2;
    }
}
```
