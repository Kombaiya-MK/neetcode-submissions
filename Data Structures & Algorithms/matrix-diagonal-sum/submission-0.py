class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        totalSum = 0
        for r in range(rows):

            totalSum += mat[r][r]
            if r + r != rows - 1:
                totalSum += mat[r][rows-r-1]
        return totalSum
        