# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

### Naive Solution

A naive approach would be to repeatedly scan the string and remove valid pairs
`()`, `{}`, and `[]` until no more can be removed.\
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

### Theoretical Connection: Pushdown Automata and Grammars

This problem is directly related to **context-free grammars (CFGs)** and
**pushdown automata (PDAs)**.

A valid sequence of parentheses can be described by a simple grammar:

`S → (S) | [S] | {S} | SS | ε`

Where:

- `S` represents a valid parentheses expression.
- `ε` (epsilon) denotes the empty string, which is considered valid.
- The rules define that a valid string can be:
  - A pair of matching brackets enclosing another valid string.
  - A concatenation of two valid strings.
  - Or an empty string.

A **pushdown automaton** is a theoretical machine similar to a finite automaton
but equipped with a **stack**, allowing it to handle nested structures.\
In this problem, the stack in our algorithm serves the same purpose: keeping
track of opening brackets that must be closed later.

Thus, our stack-based implementation is a practical example of how a
**deterministic pushdown automaton (DPDA)** recognizes the language of
well-balanced parentheses.
