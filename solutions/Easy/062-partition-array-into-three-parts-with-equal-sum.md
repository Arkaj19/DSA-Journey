# 062. Partition Array Into Three Parts With Equal Sum

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Prefix Sum |
| **Solved on** | 2026-04-26 |
| **How I got there** | Needed Hint from ChatGpt |
| **Link** | [Problem link](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/) |

---

## Problem

Given an array of integers `arr`, return `true` if we can partition the array into three **non-empty** parts with equal sums.

Formally, we can partition the array if we can find indexes `i + 1 < j` with `(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])`

**Example 1:**

```
Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
```

**Example 2:**

```
Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
```

**Example 3:**

```
Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
```

**Constraints:**

* `3 <= arr.length <= 5 * 104`
* `-104 <= arr[i] <= 104`

## My Notes & Solution

```python
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        
        n = len(arr)
        sum = 0

        if n == 1:
            return False

        for i in range(n):
            sum+= arr[i]

        target = 0

        if sum % 3 == 0:
            target = sum // 3
        else:
            return False

        curr_sum = 0
        count = 0

        for i in range(0,n):

            curr_sum+=arr[i]
            
            if curr_sum == target:
                print(curr_sum)
                curr_sum = 0
                count+=1

            if count == 2 and i != n - 1:
                return True

        return False

        
```

- Here the first thing we need to do is to find the entire sum.

- Then we need to check if it is divisible properly by 3 that means it can be divided into 3 parts.

- Now we will set the quotient as the target and then we will keep a curr_sum variable.

- As soon as we get a curr_sum = target we will increase our count.

If at any point we get that our count is 2 that is 2 partitions have been found and the index we are standing at is not the last index of the array then we can return it as true.

### 🔑 Why stopping at the second cut is enough

You already enforced:

```python
total=3×target\text{total} = 3 \times \text{target}

total=3×target
```

Now suppose during traversal you find:

- First segment sum = target

- Second segment sum = target

At that moment, you have consumed:

2×target2 \times \text{target}

2×target

---

### 🧠 What remains?

The remaining part of the array (after index i) has sum:

```plain text
remaining=total−2×target

\text{remaining} = \text{total} - 2 \times \text{target}

remaining=total−2×target
```

Substitute:

=3×target−2×target=target= 3 \times \text{target} - 2 \times \text{target} = \text{target}

=3×target−2×target=target

So mathematically, it is forced.
