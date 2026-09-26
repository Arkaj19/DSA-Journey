# 096. 1539. Kth Missing Positive Number

| | |
|---|---|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Topics** | Binary Search, Arrays |
| **Solved on** | 2026-07-28 |
| **How I got there** | Major Thinking required, Saw Video Soution |
| **Link** | _No link recorded_ |

---

## Problem

_No link was recorded for this one, so the statement couldn't be fetched automatically._

## My Notes & Solution

### Naive Solution:

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        high = max(arr)
        counter = 0
        missing_num = 0

        for i in range(1,high+1):
            if counter < len(arr):
                    
                if i == arr[counter]:
                    counter+=1
                    continue
                else:
                    missing_num+=1
                    if missing_num == k:
                        return i

        return (k - missing_num) + arr[len(arr) - 1]
```

- Here the point that I did was that it is a O(n) solution. 

- Now the fact is that I will have to maintain 2 counter variables. The counter always checkes 2 things if it has gone past the size of array and it is the main index for our arr.

- Again the ‘i’ gives us the total numbers of digits.

- Now even after everything we wont return -1. IF the number isn’t found in the arr. Then we know every subsequent value onwards is going to be a candidate for us and hence we just substract k from the missing_num and add it with the last element of the array as if saying that i need the 2nd element from the last element :

```python
Eg: 5- 3 = 2
now 2 + 6 = 8 
hence 8 is the 2nd number after 6. 
```

Binary Search

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        low = 0
        high = len( arr) - 1
        missing_num = 0
        mid = 0

        while( low <= high):

            mid = ( low + high ) // 2
            missing_num = arr[mid] - ( mid + 1)
            if missing_num < k:
                low = mid + 1
            else:
                high = mid - 1

        return low + k
```

#### Key Observation

- Binary search is performed on indices, not on the number range.

- At each index, calculate how many positive numbers are missing before arr[i].

#### Missing Count Formula

```plain text
missing_before(i) = arr[i] - (i + 1)
```

Why?

- Expected numbers till arr[i] = arr[i]

- Present numbers = i + 1

- Missing = arr[i] - (i + 1)

---

#### Binary Search

- If missing_before(mid) < k

- Else

---

#### After Binary Search

- low = first index where missing_before >= k

- Do not use mid after the loop.

- Final answer is computed using low.

---

#### Common Mistakes

- ❌ Binary search on numbers (1...max(arr)).

- ✅ Binary search on array indices.

- ❌ Use mid after loop ends.

- ✅ Use low.

- ❌ Forget formula for missing count.

- ✅ Memorize:

---

#### Binary Search Pattern

1. Compute missing_before(mid).

1. Compare with k.

1. Move low or high.

1. Use low after the loop to derive the answer.
