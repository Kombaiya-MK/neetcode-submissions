class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        transposeMatrix = [[0] * rows for _ in range(cols)]

        for c in range(cols):
            for r in range(rows):
                transposeMatrix[c][r] = matrix[r][c]
        return transposeMatrix
        