# 030. Closest Equal Element Queries

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Arrays, Binary Search, Hashing |
| **Solved on** | 2026-04-16 |
| **How I got there** | Needed Hint from ChatGpt |
| **Link** | [Problem link](https://leetcode.com/problems/closest-equal-element-queries/description/) |

---

## Problem

You are given a **circular** array `nums` and an array `queries`.

For each query `i`, you have to find the following:

* The **minimum** distance between the element at index `queries[i]` and **any** other index `j` in the **circular** array, where `nums[j] == nums[queries[i]]`. If no such index exists, the answer for that query should be -1.

Return an array `answer` of the **same** size as `queries`, where `answer[i]` represents the result for query `i`.

**Example 1:**

**Input:** nums = [1,3,1,4,1,3,2], queries = [0,3,5]

**Output:** [2,-1,3]

**Explanation:**

* Query 0: The element at `queries[0] = 0` is `nums[0] = 1`. The nearest index with the same value is 2, and the distance between them is 2.
* Query 1: The element at `queries[1] = 3` is `nums[3] = 4`. No other index contains 4, so the result is -1.
* Query 2: The element at `queries[2] = 5` is `nums[5] = 3`. The nearest index with the same value is 1, and the distance between them is 3 (following the circular path: `5 -> 6 -> 0 -> 1`).

**Example 2:**

**Input:** nums = [1,2,3,4], queries = [0,1,2,3]

**Output:** [-1,-1,-1,-1]

**Explanation:**

Each value in `nums` is unique, so no index shares the same value as the queried element. This results in -1 for all queries.

**Constraints:**

* `1 <= queries.length <= nums.length <= 105`
* `1 <= nums[i] <= 106`
* `0 <= queries[i] < nums.length`

## My Notes & Solution

```python
import bisect
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        qdict = {}
        q = len(queries)
        n = len(nums)
        ans = []


        for i in range(n):
            if nums[i] not in qdict:
                qdict[nums[i]] = []

            qdict[nums[i]].append(i)
        
        # print(qdict)
        # Now we have our dict ready with us which have each element and the indexes of their occurences
        # Now we will need to search for the elements of the queries in the dict and then we will move on the left and the right until the array length gets over aswe do for the left and the right of the cicular array

        for query in queries:
            curr_num = nums[query]
            if curr_num in qdict:
                arr = qdict[curr_num]

                # If only one element is there
                if len(arr) == 1:
                    ans.append(-1)
                    continue
                
                #This acts as a reference point around which we need to check the immidiate left and right occurences
                # pos = arr.index(query)
                pos = bisect.bisect_left(arr,query)

                # Here we get our immidiate left and right point values
                left = arr[pos - 1]
                right = arr[(pos + 1) % len(arr)]

                #Now calculating the distance between them

                d_left = abs( query - left )
                d_right = abs( query - right ) 

                # Now for checking the distance of circular case

                d_left = min(d_left, n - d_left)
                d_right = min(d_right, n - d_right)

                ans.append(min(d_left,d_right))

        return ans

```

### Steps to solve this question :

- First we implement a dict to store the index of occurences of all the elements in the nums array.

- Then we start by accessing each element of the query.

- Searching the num at that position in the array nums

- Then we check if the num is there in dict and if present we check the number of occurences.

- Finally we will return the ans array back.
