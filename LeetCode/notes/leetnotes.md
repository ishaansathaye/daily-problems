# Takeaways

## Two Sum
- Use ```enumerate()``` to get iterate through index and values
- Try to use 1-pass hash table
- Better solutions use complement to quickly find counterpart of element in list

## Add Two Numbers
- Simplify my solution by using multiple functions inside Solution class
- Use ```divmod``` to quickly find dividend and remainder between two numbers
- List comprehension ```val1  = (l1.val if l1 else 0)```
- Create link between current node and next ```result_tail.next = ListNode(out)```

## Longest String Without Repeating Characters
- Utilize **sliding window method**
- Put index of element in the hash map

## Median of Two Sorted Arrays
- Used **Binary Search on two arrays**
    - Compare elements of each array and then go to the next smallest element between two arrays
- O(log(n+m)) alternate solution
    - Uses recursion to iterate to next element in the list
        - *Uses list splicing, which is O(n), so use indices for true O(log(n+m))*
    - Helper method finds the kth element
    - Main method calls these functions depending on the length fo the combined arrays

## Rotate Image
Topics: *Matrix, Math, Transpose*
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
