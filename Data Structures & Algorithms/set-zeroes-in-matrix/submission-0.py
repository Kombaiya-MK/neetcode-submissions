class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        rowZero = [False] * rows
        colZero = [False] * cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rowZero[r] = True
                    colZero[c] = True

        for r in range(rows):
            for c in range(cols):
                if rowZero[r] or colZero[c]:
                    matrix[r][c] = 0

        
        