# 072. 1665. Minimum Initial Energy to Finish Tasks

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Hard |
| **Topics** | Arrays, Binary Search, Greedy |
| **Solved on** | 2026-05-12 |
| **How I got there** | Saw Video Soution |
| **Link** | [Problem link](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/?envType=daily-question&envId=2026-05-12) |

---

## Problem

You are given an array `tasks` where `tasks[i] = [actuali, minimumi]`:

* `actuali` is the actual amount of energy you **spend to finish** the `ith` task.
* `minimumi` is the **minimum** amount of energy you **require to begin** the `ith` task.

For example, if the task is `[10, 12]` and your current energy is 11, you cannot start this task. However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.

You can finish the tasks in **any order** you like.

Return the **minimum** initial amount of energy you will need to finish all the tasks.

**Example 1:**

```
Input: tasks = [[1,2],[2,4],[4,8]]
Output: 8
Explanation:
Starting with 8 energy, we finish the tasks in the following order:
    - 3rd task. Now energy = 8 - 4 = 4.
    - 2nd task. Now energy = 4 - 2 = 2.
    - 1st task. Now energy = 2 - 1 = 1.
Notice that even though we have leftover energy, starting with 7 energy does not work because we cannot do the 3rd task.
```

**Example 2:**

```
Input: tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
Output: 32
Explanation:
Starting with 32 energy, we finish the tasks in the following order:
    - 1st task. Now energy = 32 - 1 = 31.
    - 2nd task. Now energy = 31 - 2 = 29.
    - 3rd task. Now energy = 29 - 10 = 19.
    - 4th task. Now energy = 19 - 10 = 9.
    - 5th task. Now energy = 9 - 8 = 1.
```

**Example 3:**

```
Input: tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
Output: 27
Explanation:
Starting with 27 energy, we finish the tasks in the following order:
    - 5th task. Now energy = 27 - 5 = 22.
    - 2nd task. Now energy = 22 - 2 = 20.
    - 3rd task. Now energy = 20 - 3 = 17.
    - 1st task. Now energy = 17 - 1 = 16.
    - 4th task. Now energy = 16 - 4 = 12.
    - 6th task. Now energy = 12 - 6 = 6.
```

**Constraints:**

* `1 <= tasks.length <= 105`
* `1 <= actual​i <= minimumi <= 104`

## My Notes & Solution

- This question is based on the Binary Search on Answers theorem.

Steps and Intuition:-

- We will be using the Binary search on Answers template here

- First we will take the l and r variables.

- Then we will do the binary search

- Once we get a value we will check if it satisfies the condtion is_possible that all the tasks are possible on the basis of that value

- Then we will store it in the result and will try to reduce the right as it is already found so we will try with lesser values.

- Else we will increase the left parameter

- Now the normal tasks array wont do.

- We need to sort it on the basis of the difference between the ( min_required energy - actual energy)

- This is because if in cases there can be the (99,100) so doing this first is not economical as we are left with just 1 energy but we should try other cases first.

- Now combining this sorting technique with the binary search we will be able to get the right result.

```python
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        n = len(tasks)
        l = 0
        r = int(1e9)
        result = 0

        ## First we need to sort the task on the descending order of ( min - actual)
        tasks.sort( key = lambda x : (x[1] - x[0]), reverse = True)
        # print( tasks )

        while ( l <= r):

            mid = l + ( r - l)//2
            if self.is_possible( tasks,mid ):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result

        
    def is_possible( self, tasks, mid):

        for task in tasks:
            if task[1] <= mid:
                mid = mid - task[0]
            else:
                return False
        
        return True
         
```
