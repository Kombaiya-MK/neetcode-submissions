class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        # ans = []
        k = 1

        while left <= right and top <= bottom:

            for c in range(left, right + 1):
                arr[top][c] = k
                k += 1
            top += 1

            for r in range(top, bottom + 1):
                arr[r][right] = k
                k += 1
            right -= 1

            # Right -> Left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    arr[bottom][c] = k
                    k += 1
                bottom -= 1

            # Bottom -> Top
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    arr[r][left] = k
                    k += 1
                left += 1
        return arr
        