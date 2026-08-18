# 004. Car Pooling

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Topics** | Greedy |
| **Solved on** | 2026-03-12 |
| **How I got there** | Needed Hint from ChatGpt |
| **Link** | [Problem link](https://leetcode.com/problems/car-pooling/description/) |

---

## Problem

There is a car with `capacity` empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer `capacity` and an array `trips` where `trips[i] = [numPassengersi, fromi, toi]` indicates that the `ith` trip has `numPassengersi` passengers and the locations to pick them up and drop them off are `fromi` and `toi` respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return `true` *if it is possible to pick up and drop off all passengers for all the given trips, or* `false` *otherwise*.

**Example 1:**

```
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
```

**Example 2:**

```
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
```

**Constraints:**

* `1 <= trips.length <= 1000`
* `trips[i].length == 3`
* `1 <= numPassengersi <= 100`
* `0 <= fromi < toi <= 1000`
* `1 <= capacity <= 105`

## My Notes & Solution

#### Story Notes – Your Approach (Concise) —> Naive Approach

- Road Representation

- Sort Trips by Pickup

- Trip Details

- Segment Simulation

- Update Passenger Load

- Capacity Check

- No Drop Subtraction Needed

- Result

- Time Complexity

- Concept

```java
class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int locations_change[] = new int[1001]; // Initialized an array of 1001 locations as that is our constraint
        Arrays.sort( trips, (a,b) -> a[1] - b[1]);
        for ( int i = 0; i< trips.length; i++)
        {
            int passengers = trips[i][0];
            int pickup = trips[i][1];
            int drop = trips[i][2];

            for( int j = pickup; j<drop; j++)
            {
                locations_change[j]+=passengers;
                if(locations_change[j] > capacity)
                return false;
            }
            // locations_change[drop]-=passengers; // THis is not required because we are already stopping our loop brfore drop hence it is never calculated.
        }
        return true;
    }
}
```

### Better Approach —> Difference Array

Revision Story Points (Brief)

- Road as Timeline

- Record Pickup & Drop Events

- Sweep the Road

- Capacity Check

- Final Result

---

## What Changed Compared to Your Earlier Approach

```java
class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int locations_change[] = new int[1001]; // Initialized an array of 1001 locations as that is our constraint
        // Arrays.sort( trips, (a,b) -> a[1] - b[1]); Sorting is not needed in the difference array approach
        int current_passengers = 0;
        for ( int i = 0; i< trips.length; i++)
        {
            int passengers = trips[i][0];
            int pickup = trips[i][1];
            int drop = trips[i][2];

            locations_change[pickup]+= passengers;
            locations_change[drop]-= passengers;
        }

        for( int i = 0; i<1000; i++)
        {
            current_passengers += locations_change[i];
            if( current_passengers > capacity)
            return false;
        }
        

        return true;
    }
}
```
