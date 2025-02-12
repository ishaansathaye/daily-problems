# Takeaways

## Two Sum

- Use `enumerate()` to get iterate through index and values
- Try to use 1-pass hash table
- Better solutions use complement to quickly find counterpart of element in list

## Add Two Numbers

- Simplify my solution by using multiple functions inside Solution class
- Use `divmod` to quickly find dividend and remainder between two numbers
- List comprehension `val1  = (l1.val if l1 else 0)`
- Create link between current node and next `result_tail.next = ListNode(out)`

## Longest String Without Repeating Characters

- Utilize **sliding window method**
- Put index of element in the hash map

## Median of Two Sorted Arrays

- Used **Binary Search on two arrays**
  - Compare elements of each array and then go to the next smallest element between two arrays
- O(log(n+m)) alternate solution
  - Uses recursion to iterate to next element in the list
    - _Uses list splicing, which is O(n), so use indices for true O(log(n+m))_
  - Helper method finds the kth element
  - Main method calls these functions depending on the length fo the combined arrays

## Rotate Image

Topics: _Matrix, Math, Transpose_

- Part of Ebay Question
- Top left -> Top right -> Bottom right -> Bottom left -> Top left
- top left (i, j) to top right (j, n-1-i)
- top right (j, n-1-i) to bottom right (n-1-i, n-j-1)
- bottom right (n-1-i, n-j-1) to bottom left (n-1-j, i)
- bottom left (n-1-j, i) to top left (i, j)
- temp variable to hold one value during the rotation
- Iteration Conditions
  - Outer: n // 2 + n % 2
    - Covers rows in the **upper half** of the matrix, including middle row if n is odd
    - n % 2 reason
      - n is odd -> middle row needs to be processed b/c surrounding elements need rotation
      - n is even -> middle row is not needed
  - Inner: j -> n // 2
    - Covers columns in the left half of the matrix
    - Only process the left half b/c right half already rotated due to the swaps
- **Go through example with even and odd length matrices**

### Transpose and Reflect

- Easier solution with just swapping elements at each position (diagonal really for transpose)
- Reflect across by iterating over half the columns

## Longest Subarray

Topics: _Sliding Window, Two Pointers, Min-Max Heap_

- Heap Solution
  - Min and max heap to keep track of the smallest and largest elements in the window
  - Until less than the limit, move the left pointer to the right; removing the element that caused the window to exceed the limit
  - After remove elements from the heap that are no longer in the window
    - anything less than left pointer
- 2 Deque Solution
  - Better time complexity since we don't have to remove elements from the heap
  - Min and max for for increasing and decreasing elements
  - Order the deques first by popping anything not following rule
  - Move left pointer until the window is valid
    - Pop only if element from maxQ or minQ is the left pointer element

## Remove Element

Topics: _Two Pointers_

- Two pointer solution
  - start left at 0 and right at either end or even 0
  - 0 then check if right is not val
  - if not then swap to have all non vals on left side
  - return left point since it is the length of the new array
- Check edge cases such as length of 1 array when using original solution

## Minimum Size Subarray Sum

Topics: _Sliding Window, Binary Search_

- Binary Search Solution is O(nlogn)
- Whenever contiguous subarray getting asked -> think of sliding window
- **Read and understand question fully**
  - Asking for min length and **greater than or equal to** sum
- Solution just uses rolling sum with removing elements from left side
- Faster solution uses inside while loop to shorten window size in 1 pass

## Is Subsequence

Topics: _Two Pointers_

- Straightforward solution with 1 pointer on each string

## Is Happy Number

Topics: _Hash Set, Two Pointers, Slow-Fast Pointers_

- First solution is to just use hashset to keep track of numbers seen
- Detect cycles if in hash set
- **Use math to get digits not string manipulation or conversion**
- **Second solution is to use Hare and Tortoise algorithm**
  - Used in Problem `#142` Linked List Cycle II
  - Detect cycle in linked list
  - Slow pointer moves 1 step and fast pointer moves 2 steps
  - If cycle exists, then they will meet at some point
  - If fast pointer reaches 1, then it is a happy number

## ZigZag Conversion

Topics: _Array, String, Math, Direction_

- Original solved using empty 2D array and then filling in the values
  - Used direction to change the row index
- Faster solution: equation to calculate number of chars in each section
  - Section being straight down and diagonal up
  - Figure out that first and last rows have identical pattern jumps
  - In between rows have jumps calculated based on characters in each section
- First solution is O(#rows\*n) and second is O(n)

## Set Matrix Zeroes

Topics: _Matrix_

- Original solution straightforward with indicators in the matrix
  - Second pass to replace indicators with 0s
  - Faster solution does not need to go through all elements
- Faster solution
  - Have different checks for first row and column
  - Only change the first element in the row and column to 0 if 0 is found
  - Another pass to change elements to 0 based on first row and column
  - 2 checks after to check if first row and column need to be changed to 0

## Merge Intervals

Topics: _Array, Sorting, Rivian_

- Sorting by starting interval values
- Checking if the end of the current interval is greater than the start of the next interval
- If so, then merge the intervals
  - Max is comparing between end of array and interval
- Alternate Solution
  - Brute Force: compare each interval
  - Create graph with intervals as nodes and edges between overlapping intervals
