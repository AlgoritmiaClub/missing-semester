class DSU:
    def __init__(self, n: int):
        self.parent = [-1] * n
        self.rank = [0] * n
        self.count = 0

    def make_set(self, x: int):
        if self.parent[x] == -1:
            self.parent[x] = x
            self.rank[x] = 0
            self.count += 1

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        idx = lambda r, c: r * cols + c
        dsu = DSU(rows * cols)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dsu.make_set(idx(r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue
                if r + 1 < rows and grid[r + 1][c] == "1":
                    dsu.union(idx(r, c), idx(r + 1, c))
                if c + 1 < cols and grid[r][c + 1] == "1":
                    dsu.union(idx(r, c), idx(r, c + 1))

        return dsu.count
