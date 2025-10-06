# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome)

### Naive Solution

The way to check if a string is a valid palindrome is:

1. Remove all non-alphanumeric characters.
2. Convert everything to lowercase.
3. Reverse the string.
4. Compare the cleaned string with its reversed version.

If they are the same, the input is a valid palindrome.

- **Time Complexity:** $O(n)$, where `n` is the length of the string, since we
  traverse it to clean and reverse it.
- **Space Complexity:** $O(n)$, because we store the cleaned string.

Although simple and easy to implement, this solution uses extra memory for the
reversed copy of the string.

---

### Two-Pointer Solution

A more memory-efficient method uses the **two-pointer technique**:

1. Set two pointers: one at the beginning(`left`), and one at the end(`right`).
2. Move both pointers toward the center:
   - Skip non-alphanumeric characters.
   - Compare characters in a case-insensitive manner.
3. If at any point characters differ, it is not a palindrome.
4. If all characters match, then the string is a valid palindrome.

- **Time Complexity:** $O(n)$, as we only traverse the string once.
- **Space Complexity:** $O(1)$, since we do not create extra copies.

This is the **optimal solution**, combining linear time complexity with constant
space usage.
