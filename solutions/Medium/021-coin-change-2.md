# 021. Coin Change 2

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | DP |
| **Solved on** | 2026-04-07 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/coin-change-ii/) |

---

## Problem

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the number of combinations that make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `0`.

You may assume that you have an infinite number of each kind of coin.

The **final** answer is **guaranteed** to fit into a signed **32-bit** integer.

**Example 1:**

```
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

**Example 2:**

```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

**Example 3:**

```
Input: amount = 10, coins = [10]
Output: 1
```

**Constraints:**

* `1 <= coins.length <= 300`
* `1 <= coins[i] <= 5000`
* All the values of `coins` are **unique**.
* `0 <= amount <= 5000`

## My Notes & Solution

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.dp = {}
        return self.ways(0,coins, amount)

    def ways( self, curr_coin_idx,coins, amount):
        if amount == 0:
            return 1

        if curr_coin_idx == len(coins):
            return 0
        
        if amount < 0:
            return 0

        if (curr_coin_idx,amount) in self.dp:
            return self.dp[(curr_coin_idx,amount)] 
        
        ## Here when we take the vcoin then we dont ned to change the count of the coin by 1
        take = self.ways( curr_coin_idx, coins, amount - coins[curr_coin_idx])

        ## Here the coin count changes hence the index needs to be chnaged
        not_take = self.ways( curr_coin_idx+1, coins, amount)

        ## Here we need to return the number of combinations and hence the +
        # return take + not_take
        self.dp[(curr_coin_idx,amount)] = take + not_take
        return self.dp[(curr_coin_idx,amount)]
```

- Here the implementation is very easy.

- Since it just requires us to find the combinations of coins which can yield us the the target sum.

- Here if we take the coin then we dont increase the coin index and keep it same.

- When we will not take then in that case we increase the coin_index.

- Here the Base Cases:

- Regarding the DP application, we use a tuple of the index and the rem_amount as the key of the dict and the returned value as the value.
