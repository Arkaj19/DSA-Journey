# 009. Min Cost Climbing Stairs

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | DP |
| **Solved on** | 2026-03-22 |
| **How I got there** | Minor Thinking required, Needed Hint from ChatGpt |
| **Link** | [Problem link](https://leetcode.com/problems/min-cost-climbing-stairs/) |

---

## Problem

You are given an integer array `cost` where `cost[i]` is the cost of `ith` step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `0`, or the step with index `1`.

Return *the minimum cost to reach the top of the floor*.

**Example 1:**

```
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
```

**Example 2:**

```
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
```

**Constraints:**

* `2 <= cost.length <= 1000`
* `0 <= cost[i] <= 999`

## My Notes & Solution

One clear misconception I had in this question :
While seeing these 2 examples:



Example 1:

```plain text
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
```

Example 2:

```plain text
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
```

I felt one thing and that is wrong. 

⇒ I was thinking how in the first example 15 was taken and not 10 but then I found that its not about reaching the last step shown but the step after the last step is being spoken about.

⇒ Hence if we land on the 2nd step i.e. 20 and our total cost will become : 10 + 15 = 25 which is more than 15 but if we start at 15 then we can reach the top by crossing the last step.

⇒ In the same way if we see the example 2 :

⇒ 0 → 2 → 4 → 6 → 7 → 9 → top ( Total 6  each price 1 )

Memoization :

⇒ Here initially what i was doing illogically was that I was passing the cost.length value which would produce array index out of bounds. because cost[n] doesn’t exist.

⇒ cost[n] = minimum out of { cost[n -1] , cost[ n - 2] ).

⇒ Because we can either jump 2 steps or 1.

⇒ So if we individually take out these two values then it will be easier for us to just take out the minimum out of them.

```java
class Solution {
    private Map<Integer, Integer>mp = new HashMap<>();
    public int minCostClimbingStairs(int[] cost) {
        // int min_cost = min_cost(cost, cost.length);
        int n = cost.length;
        return Math.min( min_cost( cost, n-1), min_cost( cost, n-2));
    }

    public int min_cost( int[]cost, int n)
    {
        if( n <= 1)
        {
            return cost[n];
        }
        if( !mp.containsKey(n))
        {
            mp.put( n,cost[n] +  Math.min(min_cost(cost, n - 1 ), min_cost(cost, n - 2)));
        }
        return mp.get(n);
    }
}
```

⇒ one thing to keep in mind is that the reason I wrote :

```java
if( n <= 1)
      {
          return cost[n];
      }
```

⇒ Is because if somehow by skipping 1 or 2 when we might land directly on 1 or 0. 
⇒ We know that at these positions the user can directly start from them as per the recursion tree also. 

Tabulation : 

⇒ Here we will make use of 2 variables step 1 and step 2.

```java
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int step1 = cost[0];
        int step2 = cost[1];
        int n = cost.length;

        for ( int i = 2; i<n ; i++) // Starting from 2 because we can start from either 1 or 0
        {
            int curr = cost[i] + Math.min(step1, step2);
            step1 = step2;
            step2 = curr;
        }
        return Math.min( step1, step2);
    }
}
```

- We initialise step1 and step2 as the minimum cost to reach step 0 and step 1 respectively.

- Then starting from index 2, for each step we compute the minimum cost required to reach that step using the previous two computed states.

- We keep updating these two variables to simulate DP in O(1) space.

- Finally, since we can reach the top from either the last or second last step, we return the minimum of those two.
