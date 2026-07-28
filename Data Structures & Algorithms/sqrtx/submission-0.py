class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:

            mid = left + (right - left) // 2
            # print(mid, left, right)
            num = mid * mid
            if num == x:
                return mid
            elif num < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

        