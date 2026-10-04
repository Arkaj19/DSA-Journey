# 113. Generate Binary Strings without Adjacent Zeroes

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Recursion |
| **Solved on** | 2026-08-17 |
| **How I got there** | Major Thinking required, Needed Hint from ChatGpt |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

### 3211. Generate Binary Strings Without Adjacent Zeros — Revision Notes

#### Core Idea

Use recursion/backtracking to build the string one character at a time.

#### Base Case

When the generated string reaches length n:

```plain text
if len(current) == n:
    result.append(current)
    return
```

#### Choices

At every position:

1. Always choose 1

```plain text
solve(current + "1")
```

1. Choose 0 only if the previous character is not 0

```plain text
if len(current) == 0 or current[-1] != "0":
    solve(current + "0")
```

#### Recursion Template

```plain text
def solve(current):
    if len(current) == n:
        result.append(current)
        return

    solve(current + "1")

    if len(current) == 0 or current[-1] != "0":
        solve(current + "0")
```

#### Important Recursion Pattern

Think:

Base case → Choices → Constraint → Recursive call

For this problem:

```plain text
Build string
   ↓
Length == n?
   ↓ Yes → store & return
   ↓ No
Choose 1 → recurse
Choose 0 → only if valid → recurse
```

#### Key Learning

Don't try to memorize the code. Draw the recursion tree first, identify the choices at each node, then convert each arrow into a recursive call.
