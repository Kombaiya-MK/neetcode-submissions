class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
        ]
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return

            if grid[r][c] != "1":
                return 

            grid[r][c] = "0"

            for dr, dc in directions:
                dfs(r + dr, c + dc)


        maxlength = 0
        length = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    length +=1
                dfs(r, c)
        return length
        