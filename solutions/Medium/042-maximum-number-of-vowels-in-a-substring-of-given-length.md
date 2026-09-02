# 042. Maximum Number of Vowels in a Substring of Given Length

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Sliding Window |
| **Solved on** | 2026-04-21 |
| **How I got there** | Could solve it instantly |
| **Link** | [Problem link](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/) |

---

## Problem

Given a string `s` and an integer `k`, return *the maximum number of vowel letters in any substring of* `s` *with length* `k`.

**Vowel letters** in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

**Example 1:**

```
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
```

**Example 2:**

```
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
```

**Example 3:**

```
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
```

**Constraints:**

* `1 <= s.length <= 105`
* `s` consists of lowercase English letters.
* `1 <= k <= s.length`

## My Notes & Solution

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        n = len(s)
        curr_vowel_count = 0
        left = 0
        right = 0
        max_vowels= 0
        substr = ""
        arr = []

        while right < n:

            curr_ch = s[right]
            arr.append(curr_ch)
            if curr_ch in ['a','e','i','o','u']:
                curr_vowel_count+=1      

            while (right - left + 1) > k :
                arr.pop(0)
                if s[left] in ['a','e','i','o','u']:
                    curr_vowel_count-=1

                left+=1

            max_vowels = max(curr_vowel_count,max_vowels)
            right+=1
        
        return max_vowels
```

- Here this is also a basic question of sliding window mechanism.

- Here at all the points we keep the current count of vowels in the window.

- At the end we return the highest count of vowels at an instant.

- Here we are not computing the window size because the window size has already been fixed by the question as k = 3.
