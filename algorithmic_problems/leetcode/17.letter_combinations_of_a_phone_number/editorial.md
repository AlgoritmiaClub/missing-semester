# [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

**Let's take this into account...**

- The mapping of digits to letters is as follows (just like on a phone keypad):

| Digit | Letters    |
| ----- | ---------- |
| 2     | a, b, c    |
| 3     | d, e, f    |
| 4     | g, h, i    |
| 5     | j, k, l    |
| 6     | m, n, o    |
| 7     | p, q, r, s |
| 8     | t, u, v    |
| 9     | w, x, y, z |

Example:

Input: digits = "23" Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

- We can return the answer in any order.

### Building up to the solution

Let’s recall the main idea:

Each digit maps to multiple letters. We want all possible combinations of these
letters when arranged in order according to the digits given.

For example:

2 → ["a","b","c"] 3 → ["d","e","f"]

All possible combinations are every possible way to pick one letter from each
set:

["a","b","c"] × ["d","e","f"]

That gives:

["ad","ae","af","bd","be","bf","cd","ce","cf"]

This operation is known as the Cartesian product of two sets. Each new digit
simply extends the existing list of combinations by appending its possible
letters.

### Approach 1: Brute Force (Cartesian Product)

We can simulate this “expansion” process manually:

1. Start with an empty list res = [].
2. For each digit in the string, combine the current res with all possible
   letters that digit maps to.
3. Continue until all digits are processed.

digits = "23"

| Step | Digit | Letters | Result After Step                                      |
| ---- | ----- | ------- | ------------------------------------------------------ |
| 1    | 2     | "abc"   | ["a", "b", "c"]                                        |
| 2    | 3     | "def"   | ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"] |

At each step, the current combinations are expanded using a Cartesian merge.

### Approach 2: Recursive (Backtracking)

Alternatively, we can use backtracking, where we explore each possible letter
for a digit and recursively build the combinations.

For each digit:

1. Choose one letter.
2. Recurse to process the next digit.
3. Once all digits are processed, store the current combination.

This approach naturally explores all the conbinations.

It would be most useful to visualize it as a tree:

```bash
                ""
      /          |          \
    "a"         "b"         "c"
  /  |   \    /  |   \    /  |   \
“ad”“ae”“af”“bd”“be”“bf”“cd”“ce”“cf”
```

This tree structure models the backtracking recursion:

- At each node, choose a letter.
- Recurse to the next digit.
- Once all digits are processed, store the combination.

**Traversal Order (Backtracking)**

1. Start at the root "".
2. Choose the first letter for the first digit:
   - Pick "a".
3. Move to the second digit:
   - Pick "d" → combination "ad" (store it)
   - Backtrack to "a" and pick "e" → "ae" (store it)
   - Backtrack to "a" and pick "f" → "af" (store it)
4. Backtrack to root and pick "b":
   - "b" + "d" → "bd" (store it)
   - "b" + "e" → "be" (store it)
   - "b" + "f" → "bf" (store it)
5. Backtrack to root and pick "c":
   - "c" + "d" → "cd" (store it)
   - "c" + "e" → "ce" (store it)
   - "c" + "f" → "cf" (store it)

### Although they both achieve the same goal...

- The brute force one is easier to reason about conceptually (expand
  step-by-step).
- The backtracking one is more traditional for recursive generation problems.

# Complexity

Being:

- n = number of digits
- k = number of letters per digit (3 to 4)
- Time complexity: $O(k^n)$ — since each digit can generate up to k branches.
- Space complexity: $O(k^n)$ for storing the output combinations, and $O(n)$ for
  recursion depth (in the backtracking approach).
