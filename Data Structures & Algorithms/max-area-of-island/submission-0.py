class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(r, c):

            if not ( 0 <= r < rows and 0 <= c < cols):
                return 0

            if grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        count = 0
        for r in range(rows):
            for c in range(cols):
                count = max(count, dfs(r, c))
        return count
        