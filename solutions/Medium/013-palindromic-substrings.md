# 013. Palindromic Substrings

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | DP |
| **Solved on** | 2026-03-25 |
| **How I got there** | Saw Video Soution |
| **Link** | [Problem link](https://leetcode.com/problems/palindromic-substrings/description/) |

---

## Problem

Given a string `s`, return *the number of **palindromic substrings** in it*.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

**Example 1:**

```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

**Example 2:**

```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

**Constraints:**

* `1 <= s.length <= 1000`
* `s` consists of lowercase English letters.

## My Notes & Solution

```python
class Solution {
    public int countSubstrings(String s) {
        int l = s.length();
        int count = 0;
        int [][]arr = new int[l][l];

        // Filling the entire 2d array with -1
        for( int i = 0; i<l; i++)
        {
            Arrays.fill(arr[i], -1);
        }

        // Here we are filling all the single characters as true palindromes
        for( int i = 0; i<l; i++)
        {
            arr[i][i] = 1;
            count++;
        }

        // Now we will work on the 2 digit characters
        for( int i = 0; i<l - 1; i++)
        {
            int c1 = s.charAt(i);
            int c2 = s.charAt(i+1);

            if( c1 == c2)
            {
                arr[i][i+1] = 1;
                count++;
            }
            else
            {
                arr[i][i+1] = 0;
            }
        }

        // Now we will work on all the substrings
        for( int n = 3; n<=l; n++)
        {
            for( int i = 0; i<=l-n; i++)
            {
                int j = i + n -1;
                if( s.charAt(i) == s.charAt(j) && arr[i+1][j-1] == 1)
                {
                    arr[i][j] = 1;
                    count++;
                }
            }
        }
        return count;
    }
}
```

→ Here basically we need to assign the single characters as individually being palindromes.
→ THen we will check the adjacent characters such that we are taking pairs like : 0,1 —- 1,2 —— 2,3 … Like this.
→ THen we will be checking for the other lengths but going gradually like all the 3 lengths first and then the 4 length and then on…

```python
// Now we will work on all the substrings
        for( int n = 3; n<=l; n++)
        {
            for( int i = 0; i<=l-n; i++)
            {
                int j = i + n -1;
                if( s.charAt(i) == s.charAt(j) && arr[i+1][j-1] == 1)
                {
                    arr[i][j] = 1;
                    count++;
                }
            }
        }
```

→ In this code snippet we are looping according to the size i.e. 3 size first and then 4 size and then 5 size.
