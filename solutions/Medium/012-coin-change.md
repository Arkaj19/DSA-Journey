# 012. Coin Change

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | DP |
| **Solved on** | 2026-03-24 |
| **How I got there** | Saw Video Soution |
| **Link** | [Problem link](https://leetcode.com/problems/coin-change/) |

---

## Problem

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the fewest number of coins that you need to make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

**Example 1:**

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

**Example 2:**

```
Input: coins = [2], amount = 3
Output: -1
```

**Example 3:**

```
Input: coins = [1], amount = 0
Output: 0
```

**Constraints:**

* `1 <= coins.length <= 12`
* `1 <= coins[i] <= 231 - 1`
* `0 <= amount <= 104`

## My Notes & Solution

⇒ This is an optimization problem so first thing should come to brain is using greedy but can we actually do it.
⇒ But in a case like this : 

```plain text
amount = 6 , coins = [1,3,4]

6 - 4 = 2
2 - 1 = 1
1 - 1 = 1

Hence 3 coins 

but the right answer is :

3 + 3 = 2 coins 
```

⇒ Hence we can say that this is not a problem that can be solved by using greedy.
⇒ We need to be able to explore all the ways.

⇒ So the recurrence relation can be : 1 + min to reach to particulat number as we know that since we are going 1 down hence 1 needs to be added.


→ At present this brute force recursive method will give us a time complexity of no.of.coins to the power of amount branches which is a lot.

example : 2^100 = 1267650600228229401496703205376
This is a big number and hence we will be applying DP here.

```javascript
class Solution {
    public int coinChange(int[] coins, int amount) {
        int res = coin_helper(coins, amount);
        return res;
    }

    public int coin_helper( int[]coins, int amt)
    {
        if( amt == 0)
        return 0;

        if ( amt < 0)
        return -1;

        int min = Integer.MAX_VALUE;
        for( int i=0; i<coins.length; i++)
        {
            int res = coin_helper( coins, amt - coins[i]);
            if( res != -1 )
            {
                min = Math.min( min, 1 + res); // “Among all possible choices, keep the minimum number of coins needed”
            }
        }

        if ( min == Integer.MAX_VALUE)
        return -1;
        else
        return min;
    }
}
```

⇒ Dp implementation ( Recursive —> Memoization )

```java
class Solution {
    private Map<Integer, Integer> mp = new HashMap<>();

    public int coinChange(int[] coins, int amount) {
        int res = coin_helper(coins, amount);
        return res;
    }

    public int coin_helper(int[] coins, int amt) {
        if (amt == 0)
            return 0;

        if (amt < 0)
            return -1;

        int min = Integer.MAX_VALUE;

        if (mp.containsKey(amt)) // If the value is already present just return it
            return mp.get(amt);

        for (int i = 0; i < coins.length; i++) {

            int res = coin_helper(coins, amt - coins[i]);
            if (res != -1) {
                min = Math.min(min, 1 + res); // “Among all possible choices, keep the minimum number of coins needed”
            }
        }

        if (min == Integer.MAX_VALUE)
            mp.put(amt, -1); // If at the end the min remains infintiy just return -1
        else
            mp.put(amt, min); // Just return the min in a valid case

        return mp.get(amt);
    }
}
```

### 🔁 Step-by-Step Thinking (Very Important)

#### 1. Sabse pehle kya karta hai?

```plain text
Agar amount = 0 → kuch nahi chahiye → answer = 0
```

👉 “Arre bhai kuch banana hi nahi hai toh coins kyun lagenge?”

---

#### 2. Agar amount negative ho gaya

```plain text
→ galat rasta
```

👉 “Zyada subtract kar diya → yeh path bekaar hai”

---

#### 3. Ab main kaam shuru hota hai

Tu bolta hai:

> “Main har coin try karunga”

---

#### 4. Har coin ke liye kya karta hai?

```plain text
coin uthaya → amount se minus kiya → baaki ka problem solve kiya
```

👉 Matlab:

> “Agar main yeh coin use karu toh baaki ka kaam kitne coins me hoga?”

---

#### 5. Yeh line sabse important hai

```plain text
min = Math.min(min, 1 + res)
```

👉 Iska matlab:

> “Is coin ko use karunga → 1 coin laga

---

### 🔁 Real Life Analogy

Soch:

Tu ₹11 banana chah raha hai using coins [1,2,5]

Tu try karta hai:

- “Agar 5 le liya → baaki 6 banana hai”

- “Agar 2 le liya → baaki 9 banana hai”

- “Agar 1 le liya → baaki 10 banana hai”

👉 Har choice ke baad tu bolta hai:

> “Chalo dekhte hain kaunsa option sabse kam coins me kaam khatam karta hai”

---

### 🧠 Memoization (Sabse Important Part)

“Arre dekh, yeh sabse smart part hai”

Tu bolta hai:

> “Agar maine pehle hi kisi amount ka answer nikaal liya hai…”

👉 Toh:

```plain text
dobara calculate nahi karunga
seedha map se utha lunga
```

---

#### 🔥 Example

```plain text
f(6) ek baar calculate kiya → answer = 2
```

Next time:

```plain text
f(6) aaye → direct 2 return
```

👉 “Time bachao, life easy banao”

---

### 🎯 Final Flow (Super Simple)

“Arre dekh pura flow yaad rakh:”

1. Agar amount 0 → return 0

1. Agar amount < 0 → return -1

1. Agar pehle se answer hai → map se le lo

1. Har coin try karo

1. Best answer nikaalo

1. Map me store karo

1. Return karo

---

### 🧠 One-Line Memory Trick

> “Har amount ke liye pooch: isko banane ka sabse sasta tareeka kya hai?”

---

### 💡 Ultimate Intuition

- Tu decision tree explore kar raha hai

- DP bolta hai:

---

### 🎯 Final Feeling You Should Have

> “Main har coin try karta hoon, best choose karta hoon, aur future ke liye store karta hoon”
