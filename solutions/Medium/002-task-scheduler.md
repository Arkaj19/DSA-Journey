# 002. Task Scheduler

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Greedy |
| **Solved on** | 2026-03-12 |
| **How I got there** | Saw Video Soution |
| **Link** | [Problem link](https://leetcode.com/problems/task-scheduler/) |

---

## Problem

You are given an array of CPU `tasks`, each labeled with a letter from A to Z, and a number `n`. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of **at least** `n` intervals between two tasks with the same label.

Return the **minimum** number of CPU intervals required to complete all tasks.

**Example 1:**

**Input:** tasks = ["A","A","A","B","B","B"], n = 2

**Output:** 8

**Explanation:** A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

**Example 2:**

**Input:** tasks = ["A","C","A","B","D","B"], n = 1

**Output:** 6

**Explanation:** A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

**Example 3:**

**Input:** tasks = ["A","A","A", "B","B","B"], n = 3

**Output:** 10

**Explanation:** A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

**Constraints:**

* `1 <= tasks.length <= 104`
* `tasks[i]` is an uppercase English letter.
* `0 <= n <= 100`

## My Notes & Solution

- Basic Mathematics is enough to solve this problem : 
 resultant = ( n+1 ) * ( max.f - 1 ) + count of max .freq encountered

- Here but finally while returning we need to return the maximum of the tasks array length and the calculated result.

Things to be rememebered for future:

- Cycles.

- Corner Cases.

- Count of the Max Frequency.

- Check the max out of the freq of max or the array size.

- The main thing that most people don’t think is that even a mathematical formula can be created.

- Basic mathematics is enough to solve this problem: resultant = (n + 1) × (max_freq − 1) + count of max_freq encountered.

- When returning the result, we need to return the maximum of the tasks array length and the calculated result.

- This is because when the interval is 1 or less and the max frequency is also low, the calculated result might be smaller than the tasks array size—which is impossible.

- This is greedy because we schedule the task with the maximum frequency first.

- The result should always be at least the size of the tasks array.

- Example:Input: tasks = ["A","C","A","B","D","B"], n = 1According to our formula, the answer is:

= (n + 1) × (max_freq − 1) + count_max_freq

= 4 < 6 (array size)

- This is not possible.

```java
class Solution {
   public int leastInterval(char[] tasks, int n) {
       Map<Character,Integer>mp = new HashMap<>();
       for( int i = 0; i<tasks.length; i++)
       {
           char ch = tasks[i];
           if( mp.containsKey(ch))
           {
               mp.put(ch,mp.get(ch) + 1);
           }
           else
           {
               mp.put(ch,1);
           }
       }
       // Here we have all the frequencies
       int max = 0;
       int count_max = 0;
       for (char key : mp.keySet()) {
           int value= mp.get(key);
           if( value > max)
           {
               max = value;
               count_max = 1;
           }
           else if ( value == max)
           {
               count_max++;
           }
       }
       // System.out.println("max is " + max);
       // System.out.println("max count is " + count_max);

       int res = ((n + 1) * (max - 1)) + count_max;
       return Math.max(tasks.length,res);
   }
}

```
