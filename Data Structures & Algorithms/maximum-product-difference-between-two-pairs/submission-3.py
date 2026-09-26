class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0
        min1 = float('inf')
        min2 = float('inf')

        for num in nums:
            if num >= max1:
                max2 = max1
                max1 = num
            elif num < max1 and num > max2:
                max2 = num
            
            if num <= min1:
                min2 = min1
                min1 = num
            elif num > min1 and num < min2:
                min2 = num
        print(max1, max2, min1, min2)
        return max1 * max2 - min1 * min2
        