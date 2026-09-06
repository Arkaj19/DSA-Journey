# 052. Traffic Signal Color

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Strings |
| **Solved on** | 2026-04-23 |
| **How I got there** | Could solve it instantly |
| **Link** | [Problem link](https://leetcode.com/problems/traffic-signal-color/description/) |

---

## Problem

You are given an integer `timer` representing the remaining time (in seconds) on a traffic signal.

The signal follows these rules:

* If `timer == 0`, the signal is `"Green"`
* If `timer == 30`, the signal is `"Orange"`
* If `30 < timer <= 90`, the signal is `"Red"`

Return the current state of the signal. If none of the above conditions are met, return `"Invalid"`.

**Example 1:**

**Input:** timer = 60

**Output:** "Red"

**Explanation:**

Since `timer = 60`, and `30 < timer <= 90`, the answer is `"Red"`.

**Example 2:**

**Input:** timer = 5

**Output:** "Invalid"

**Explanation:**

Since `timer = 5`, it does not satisfy any of the given conditions, the answer is `"Invalid"`.

**Constraints:**

* `0 <= timer <= 1000`

## My Notes & Solution

```python
class Solution:
    def trafficSignal(self, timer: int) -> str:

        if timer == 0:
            return "Green"

        elif timer == 30:
            return "Orange"

        elif timer > 30 and timer <= 90:
            return "Red"

        else:
            return "Invalid"

```
