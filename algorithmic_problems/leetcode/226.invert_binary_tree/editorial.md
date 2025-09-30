# [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

### Problem Insight

The core idea is simple: for each node in the tree, swap its left and right
children. This can be achieved through any form of traversal — depth-first or
breadth-first. Since every node is processed once and only requires a local
swap, the solution is straightforward.

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
