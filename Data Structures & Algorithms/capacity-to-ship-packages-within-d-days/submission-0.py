class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:  
        def feasible(n):
            dayCount = 1
            currSum = 0

            for weight in weights:
                if currSum + weight > n:
                    currSum = weight
                    dayCount += 1
                else:
                    currSum += weight
            # print(dayCount)
            return dayCount <= days

        left = max(weights)
        right = sum(weights)

        while left < right:

            mid = left + (right - left) // 2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        # print(left, right, mid)
        return right
            