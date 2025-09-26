# [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

**Problem.** Given the head of a singly linked list, reverse the list and return
the new head.

## Building up intuition

Reversing a singly linked list means making every next pointer point
“backwards.” Because nodes are singly linked, you can only walk forward, so when
you flip an edge you must first save the original `next` pointer somewhere. Two
standard ways to do this are an iterative two-pointer scan or a recursive unwind
from the tail.

## Iterative (two-pointer) approach

Walk the list with a current pointer `curr`, and maintain `prev` as the head of
the already-reversed prefix. On each step:

1. save `curr.next` in a temporary variable `nxt`,
2. redirect `curr.next = prev`,
3. advance `prev = curr` and `curr = nxt`.\
   When `curr` becomes `None`, `prev` is the new head.

**Correctness (invariant).** After each iteration, the sublist starting at
`prev` is exactly the reversal of the original prefix up to the previous `curr`.
Each original edge is reversed once, and no pointers are lost because `nxt`
preserves the forward link before rewiring. When the loop ends, the entire list
has been reversed and `prev` is the new head.

**Complexity.** Time $O(n)$, extra space $O(1)$.

## Recursive approach

Recurse to the tail so that the call for `head.next` returns the head of the
reversed suffix. On the way back, attach `head` to the end of that suffix by
setting `head.next.next = head`, and cut the original forward link with
`head.next = None` to avoid a cycle. Return the `new_head` obtained from the
recursive call.

**Correctness.** The recursive call produces a correctly reversed suffix. The
two pointer assignments reattach the current node to the end of that suffix
while preserving acyclicity, yielding a fully reversed list at the top level.

**Complexity.** Time $O(n)$, extra space $O(n)$ due to the recursion stack
(Python lacks TCO). Prefer the iterative version for large lists to avoid depth
limits.

## Summary

- Iterative two-pointer: time $O(n)$, space $O(1)$ — recommended in Python.
- Recursive: time $O(n)$, space $O(n)$ — concise but stack-bounded.
