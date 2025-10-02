# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

### Naive Solution

The naive idea is to repeatedly scan the string and remove valid pairs `()`,
`{}`, and `[]` until no more can be removed.\
If the string becomes empty, it is valid. Otherwise, it is invalid.

This approach, however, involves repeatedly traversing and modifying the string,
which can lead to a worst-case complexity of $O(n^2)$.

### Stack Solution

A better solution uses a **stack** to ensure proper matching of parentheses in
one pass.

- Iterate over each character:
  - If it is an opening bracket (`(`, `{`, `[`), push it onto the stack.
  - If it is a closing bracket (`)`, `}`, `]`), check the top of the stack:
    - If the stack is empty, the string is invalid.
    - If the top of the stack matches the corresponding opening bracket, pop it.
    - Otherwise, it is invalid.

At the end:

- If the stack is empty, the string is valid.
- If not, there are unmatched brackets, so it is invalid.

The complexity is $O(n)$ because:

- Each character is processed once.
- Each character is pushed and popped at most once.
