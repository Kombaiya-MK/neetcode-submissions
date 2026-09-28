class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq = {}
        n = len(grid)
        for idx in range(n*n):
            freq[idx+1] = -1
        ans = [0, 0]
        for row in range(n):
            for col in range(n):
                if grid[row][col] in freq:
                    freq[grid[row][col]] += 1

        for num in freq:
            if freq[num] == -1:
                ans[1] = num
            if freq[num] == 1:
                ans[0] = num
        return ans
        

        