# 007. Fibonacci Series

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | DP |
| **Solved on** | 2026-03-15 |
| **How I got there** | Saw Video Soution |
| **Link** | [Problem link](https://leetcode.com/problems/fibonacci-number/description/) |

---

## Problem

The **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,

```
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
```

Given `n`, calculate `F(n)`.

**Example 1:**

```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```

**Example 2:**

```
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
```

**Example 3:**

```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

**Constraints:**

* `0 <= n <= 30`

## My Notes & Solution

Here the question can be done in 2 different dp Ways:

1. Memoization ( Top - Down )

```java
class Solution {
    private Map<Integer,Integer>mp = new HashMap<>();
    public int fib(int n) {
        if( n <= 1)
            return n;
        if( !mp.containsKey(n))
        {
            mp.put(n, (fib(n - 1) + fib(n - 2)));
        }
        return mp.get(n);
    }
}
```

1. Tabulation ( Bottom - Up )

```java
class Solution {
    public int fib(int n) {

        if (n == 0) return 0;
        if (n == 1) return 1;
        int num1 = 0;
        int num2 = 1;
        for( int i = 2; i<=n; i++)
        {
            int curr = num1 + num2;
            num1 = num2;
            num2 = curr;
        }
        return num2;
    }
}
```
