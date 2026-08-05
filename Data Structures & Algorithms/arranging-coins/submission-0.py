class Solution:
    def arrangeCoins(self, n: int) -> int:

        def feasible(num):
            sumOfNum = (num * (num + 1)) // 2
            return sumOfNum <= n

        left, right = 1, n

        while left < right:

            mid = left + (right - left + 1) // 2
            if feasible(mid):
                left = mid
            else:
                right = mid - 1
        return left