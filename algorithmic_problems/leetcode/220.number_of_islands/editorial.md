# [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

### Naive Solution

A naive approach would be to scan the grid for every cell with value `1` and
explore all possible connected paths repeatedly, marking islands multiple times.
This redundant exploration yields very poor performance, as the same land cells
would be revisited many times.

### Depth-First Search (sol 1)

A more efficient method is to treat the grid as a graph where land cells are
nodes connected in four directions (up, down, left, right). We scan the grid
once, and each time we find an unvisited land cell, we launch a DFS that marks
all reachable land in that component as visited. Each DFS call corresponds to
discovering one new island.

### Breadth-First Search (sol 2)

Alternatively, BFS can be used instead of DFS. Starting from an unvisited land
cell, we perform a level-order traversal with a queue, exploring neighbors and
marking them visited. This avoids recursion depth issues and processes each
island iteratively.

### Complexity

Both DFS and BFS approaches have the same asymptotics:

- **Time:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid.
  Each cell is visited at most once.
- **Space:** $O(m \cdot n)$ in the worst case for the visited set, plus
  recursion depth up to $O(m \cdot n)$ (DFS) or queue size up to $O(m \cdot n)$
  (BFS).
