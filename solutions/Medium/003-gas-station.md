# 003. Gas Station

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Greedy |
| **Solved on** | 2026-03-12 |
| **How I got there** | Needed Hint from ChatGpt |
| **Link** | [Problem link](https://leetcode.com/problems/gas-station/description/) |

---

## Problem

There are `n` gas stations along a circular route, where the amount of gas at the `ith` station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `ith` station to its next `(i + 1)th` station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return *the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return* `-1`. If there exists a solution, it is **guaranteed** to be **unique**.

**Example 1:**

```
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
```

**Example 2:**

```
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
```

**Constraints:**

* `n == gas.length == cost.length`
* `1 <= n <= 105`
* `0 <= gas[i], cost[i] <= 104`
* The input is generated such that the answer is unique.

## My Notes & Solution

- A prefix sum needs to be maintained.


Here are clean revision story notes you can keep for this problem.

---

## Gas Station – Revision Story Notes

#### Problem Understanding

- We are given two arrays:

- We must find the starting station index from which we can complete the entire circular route.

- If it is not possible, return 1.

- The problem guarantees that if a solution exists, it will be unique.

---

## Key Observations

#### 1. Global Feasibility Condition

- First check if completing the circuit is even possible.

```plain text
Total Gas ≥ Total Cost
```

- If:

```plain text
total_gas < total_cost
```

→ There is not enough fuel in the entire system to complete the circuit.

So we immediately:

```plain text
return -1
```

✅ This condition handles the case where no solution exists.

(This answered my doubt about “how the algorithm returns -1 if no station works”.)

---

#### 2. Convert Problem into Gain/Loss

Think in terms of net gain:

```plain text
gain[i] = gas[i] - cost[i]
```

While travelling:

```plain text
tank += gain[i]
```

---

#### 3. Greedy Insight

If starting from station A we run out of gas at station B, then:

```plain text
None of the stations between A and B can be a valid starting point.
```

Reason:

- Starting later gives even less accumulated fuel, so they must also fail.

Therefore we skip all those stations.

---

#### 4. Greedy Traversal Logic

Maintain two variables:

```plain text
start → candidate starting station
sum   → current tank balance
```

While iterating stations:

1. Add the gain:

```plain text
sum += gas[i] - cost[i]
```

1. If the tank becomes negative:

```plain text
sum < 0
```

then:

- Current start cannot work

- Move start to next station

```plain text
start = i + 1
sum = 0
```

---

#### 5. Final Result

- Because we already ensured:

```plain text
total_gas ≥ total_cost
```

a valid solution must exist.

So we simply return:

```plain text
start
```

---

## Time & Space Complexity

```plain text
Time  : O(n)
Space : O(1)
```

Only one pass after computing totals.

Code :

```java
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {

        int total_gas = 0;
        int total_cost = 0;

        for( int i = 0; i<gas.length; i++)
        {
            total_gas+= gas[i];
            total_cost+=cost[i];
        }

        if( total_gas < total_cost )
        return -1;

        int sum = 0;
        int start = 0;
        for( int i = 0; i<gas.length; i++)
        {
            int curr_sum = gas[i] - cost[i];
            sum+= curr_sum;
            if( sum < 0)
            {
                start = i+1;
                sum = 0;
            }
        }

        return start;
    }
}
```
