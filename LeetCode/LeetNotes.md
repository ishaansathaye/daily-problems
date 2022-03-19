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