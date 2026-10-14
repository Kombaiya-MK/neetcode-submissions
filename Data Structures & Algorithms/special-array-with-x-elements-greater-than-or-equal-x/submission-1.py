class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def isValid(n):
            count = 0
            for num in nums:
                if num >= n:
                    count += 1
            return count
        
        left = 1
        right = len(nums)
        
        while left <= right:
            mid = left + (right - left) // 2
            count = isValid(mid)  
            # print(mid, count)
            if count == mid:
                return mid
            if count < mid:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        