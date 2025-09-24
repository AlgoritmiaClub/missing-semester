# [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

### Naive Solution

A straightforward approach is to visit every node in the tree and swap its left
and right children. This can be done with either depth-first or breadth-first
traversal. The operation is local and requires no extra computation beyond the
swap itself.

### Recursive DFS (sol 1)

The recursive method applies the swap at the current node and then recurses into
the left and right subtrees. The base case is when the node is `null`. This is
the simplest and most direct implementation, though it may hit recursion depth
limits on very skewed trees.

### Iterative Traversal (sol 2)

To avoid recursion limits, an iterative solution using a stack (DFS) or a queue
(BFS) can be used. Each node is processed once: swap its children, then push its
non-null children for later processing.

### Complexity

Both recursive and iterative solutions share the same asymptotics:

- **Time:** $O(n)$, since each of the $n$ nodes is visited once.
- **Space:** $O(h)$, where $h$ is the height of the tree.
  - Recursive: stack frames up to $h$.
  - Iterative: queue/stack size up to $h$.
