# 040. Fruits Into Baskets

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Sliding Window |
| **Solved on** | 2026-04-20 |
| **How I got there** | Needed Hint from ChatGpt |
| **Link** | [Problem link](https://leetcode.com/problems/fruit-into-baskets/) |

---

## Problem

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the **type** of fruit the `ith` tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

* You only have **two** baskets, and each basket can only hold a **single type** of fruit. There is no limit on the amount of fruit each basket can hold.
* Starting from any tree of your choice, you must pick **exactly one fruit** from **every** tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
* Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array `fruits`, return *the **maximum** number of fruits you can pick*.

**Example 1:**

```
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
```

**Example 2:**

```
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
```

**Example 3:**

```
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
```

**Constraints:**

* `1 <= fruits.length <= 105`
* `0 <= fruits[i] < fruits.length`

## My Notes & Solution

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        n = len(fruits)
        left = 0
        right = 0
        basket_dict = {}
        max_basket_size = 0
        basket = 0

        while right < n:
            
            curr_fruit = fruits[right]

            basket_dict[curr_fruit] = basket_dict.get(curr_fruit,0) + 1

            while( len(basket_dict) > 2):
                if basket_dict[fruits[left]] == 1:
                    del basket_dict[fruits[left]]
                else:
                    basket_dict[fruits[left]]-=1
                left+=1

            basket = right - left + 1
            max_basket_size = max(max_basket_size, basket)
            right+=1


        return max_basket_size
```

- Here this is a classic sliding window problem that we just solved.

- Initially we will be taking in all the fruits and increase their count if present or add a key if new.

- Then we will increase the right by 1.

- But very very important that is we wont be calculating the max_bucket_size here because if the max_bucket increases here then after the correction of the window it will become erroneous 

- Then just like other sliding window questions we will run a while loop which will rectify the erroneous windows and delete either the entire key if the count of it has come to 1 or reduct the count by 1.

```python
if basket_dict[fruits[left]] == 1:
	  del basket_dict[fruits[left]]
else:
	  basket_dict[fruits[left]]-=1
```

- Finally we calculate the correct window size and then find the max_window size.

- Finally we move the right pointer by 1.
