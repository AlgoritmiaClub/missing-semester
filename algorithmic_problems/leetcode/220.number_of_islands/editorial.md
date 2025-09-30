# [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

### Naive Solution

A naive approach would be to scan the grid for every cell with value `1` and
explore all possible connected paths repeatedly, marking islands multiple times.
This redundant exploration yields very poor performance, as the same land cells
would be revisited many times.

- **Time:** In the worst case, each land cell could be revisited for every
  neighboring cell that triggers a fresh exploration. This can blow up to
  roughly $O((m \cdot n)^2)$ in pathological cases, since each DFS/BFS
  exploration may re-scan large parts of the grid redundantly.
- **Space:** $O(1)$ beyond the input grid, as no persistent visited tracking is
  maintained.

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

### Disjoint Set Union (sol 3)

Another alternative is to use **Disjoint Set Union (Union-Find)**. We treat each
land cell as a node and union it with its neighboring land cells. At the end,
the number of distinct connected components (roots) gives the number of islands.

### Complexity

- **Naive:** Up to $O((m \cdot n)^2)$ time, $O(1)$ space.
- **DFS (sol 1) / BFS (sol 2):** $O(m \cdot n)$ time, $O(m \cdot n)$ space.
- **DSU (sol 3):** $O(m \cdot n \cdot \alpha(m \cdot n))$ time (almost linear,
  where $\alpha$ is the inverse Ackermann function), $O(m \cdot n)$ space.
