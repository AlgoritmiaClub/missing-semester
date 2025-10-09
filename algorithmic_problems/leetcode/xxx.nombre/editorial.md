# [xxx. Nombre](https://leetcode.com/problems/daily-temperatures/)

### Naive Solution

The naive approach would be to iterate over every number, and count until there
is a number less than that one. As we perform two nested linear searches, the
complexity if $O(n^2)$.

### Monotonic Stack

Instead of the nested search, we can use a monotonic decreasing stack which
stores the indexes of the elements in decreasing order by value. We iterate over
the numbers and push to the stack while we go, on each push, we maintain the
monotonic invariant by popping elements less than the current one.

When an element is popped, the current element is guaranteed to be its next
greater element:

- If there had been a greater element earlier, that element would already have
  caused the pop.
- Since that did not happen, the current element is the first greater element to
  the right.

The complexity is $O(n)$, because we iterate over the elements once, and each
element is pushed and popped once.
