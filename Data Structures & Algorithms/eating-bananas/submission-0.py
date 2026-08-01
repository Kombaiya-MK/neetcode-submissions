class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canFinish(n):
            minHours = 0
            for pile in piles:
                minHours += math.ceil(pile/n)
            return minHours <= h
        left = 1
        right = max(piles)

        while left < right:

            mid = left + (right - left)//2

            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        return right
            