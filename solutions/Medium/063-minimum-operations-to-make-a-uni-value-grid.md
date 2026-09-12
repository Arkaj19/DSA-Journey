# 063. Minimum Operations to Make a Uni-Value Grid

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Math, Grid, Median Calculation |
| **Solved on** | 2026-04-27 |
| **How I got there** | Needed Hint from ChatGpt |
| **Link** | [Problem link](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/?envType=daily-question&envId=2026-04-28) |

---

## Problem

You are given a 2D integer `grid` of size `m x n` and an integer `x`. In one operation, you can **add** `x` to or **subtract** `x` from any element in the `grid`.

A **uni-value grid** is a grid where all the elements of it are equal.

Return *the **minimum** number of operations to make the grid **uni-value***. If it is not possible, return `-1`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/09/21/gridtxt.png)

```
Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/09/21/gridtxt-1.png)

```
Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2021/09/21/gridtxt-2.png)

```
Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 105`
* `1 <= m * n <= 105`
* `1 <= x, grid[i][j] <= 104`

## My Notes & Solution

- Here we first need to unpack our grid into a basic 1d array first because there is actually no need of the gird.

- Then here one thing is for sure and that is if the remainders of the number on being divided by x is not the same then one thing is for sure that they will never be equal.

- Then we will sort the arrray.

- Then we will get the median among them such that the smaller can be raised to the median number and the numbers bigger than the median can be reduced to it which will provide optimal choice for us.

- Finally for each operation we will increase our count and finally return the count.

```python
for num in nums:
	  while num != common:
	      if num < common:
	          num+=x
	          count+=1
	      elif num > common:
	          num-=x
	          count+=1
	          
- This I had done first but this is logical but it will throw TLE.
- Hence we changed the while loop to just this.

#---------------------------------------------------------------------
#---------------------------------------------------------------------

count+= abs( num - common)// x

- It basically means that the difference between the number and the median divided by x will give us the count of operations required.

```


Hence the code is : 


```python
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        nums = []

        for i in range( len(grid)):
            for j in range( len( grid[i])):
                nums.append(grid[i][j])

        print(nums)

        remainder = nums[0] % x

        for i in range(1,len(nums)):
            if nums[i] % x != remainder:
                return -1
                break
        
        count = 0
        nums.sort()

        common = nums[len(nums)//2]

        for num in nums:
            count+= abs( num - common)// x
            
        return count
```
