# 046. Words Within Two Edits of Dictionary

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Strings |
| **Solved on** | 2026-04-22 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/words-within-two-edits-of-dictionary/description/?envType=daily-question&envId=2026-04-22) |

---

## Problem

You are given two string arrays, `queries` and `dictionary`. All words in each array comprise of lowercase English letters and have the same length.

In one **edit** you can take a word from `queries`, and change any letter in it to any other letter. Find all words from `queries` that, after a **maximum** of two edits, equal some word from `dictionary`.

Return *a list of all words from* `queries`*,* *that match with some word from* `dictionary` *after a maximum of **two edits***. Return the words in the **same order** they appear in `queries`.

**Example 1:**

```
Input: queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
Output: ["word","note","wood"]
Explanation:
- Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
- Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
- It would take more than 2 edits for "ants" to equal a dictionary word.
- "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
Thus, we return ["word","note","wood"].
```

**Example 2:**

```
Input: queries = ["yes"], dictionary = ["not"]
Output: []
Explanation:
Applying any two edits to "yes" cannot make it equal to "not". Thus, we return an empty array.
```

**Constraints:**

* `1 <= queries.length, dictionary.length <= 100`
* `n == queries[i].length == dictionary[j].length`
* `1 <= n <= 100`
* All `queries[i]` and `dictionary[j]` are composed of lowercase English letters.

## My Notes & Solution

```python
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        qsize = len(queries)
        dict_size = len(dictionary)
        i = 0
        j = 0
        count = 0
        res = []

        for idx,query in enumerate(queries):
            for word in dictionary:
                count = 0
                for ch in range(len(word)):
                    if query[ch] != word[ch]:
                        count+=1
                    else:
                        continue
                
                if count <= 2:
                    res.append(query)
                    break
            if query in res:
                continue

        return res
```

- Here the best optimal solution is to go for the 3 loops where every word of the query is matched with the dictionary and each character of the query word is checked with characters of each word of the dictionary.
