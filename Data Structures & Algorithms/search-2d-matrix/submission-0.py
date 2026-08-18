class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:

            mid = left + (right - left) // 2

            midRow = mid // cols
            midCol = mid % cols

            if matrix[midRow][midCol] == target:
                return True

            elif matrix[midRow][midCol] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False

        