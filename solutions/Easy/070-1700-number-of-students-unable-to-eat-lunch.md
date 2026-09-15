# 070. 1700. Number of Students Unable to Eat Lunch

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Queue, Stack, Arrays |
| **Solved on** | 2026-05-07 |
| **How I got there** | Minor Thinking required |
| **Link** | [Problem link](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/) |

---

## Problem

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers `0` and `1` respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a **stack**. At each step:

* If the student at the front of the queue **prefers** the sandwich on the top of the stack, they will **take it** and leave the queue.
* Otherwise, they will **leave it** and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays `students` and `sandwiches` where `sandwiches[i]` is the type of the `i​​​​​​th` sandwich in the stack (`i = 0` is the top of the stack) and `students[j]` is the preference of the `j​​​​​​th` student in the initial queue (`j = 0` is the front of the queue). Return *the number of students that are unable to eat.*

**Example 1:**

```
Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.
```

**Example 2:**

```
Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3
```

**Constraints:**

* `1 <= students.length, sandwiches.length <= 100`
* `students.length == sandwiches.length`
* `sandwiches[i]` is `0` or `1`.
* `students[i]` is `0` or `1`.

## My Notes & Solution

```python
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        

        sand_len = len(sandwiches)
        stud_len = len(students)

        count = 0

        while sand_len > 0:

            if count == len(students):
                return len(students)
            
            # print( students[0], sandwiches[0])
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                # print( students)
                # print( sandwiches)
                count = 0

            else:
                student = students.pop(0)
                students.append(student)
                count+=1

        return len(students)
```

- Here the main logic is that if the student doesn’t takes a sandwich then he has to be sent at the last of the queue.

- If he takes a sandwich then he and the sandwich leave the arrays.

- Now we need to keep a count because it can happen that nobody took the sandwiches and if we continuosly keep on adding the people at the end of the list then it will become a never ending list.

- Hence we need to keep a count that if the count value equals the number of the students in the array then we can say that nobody liked the sandwiches and we can break out at that moment right by returning the len of the students array.
