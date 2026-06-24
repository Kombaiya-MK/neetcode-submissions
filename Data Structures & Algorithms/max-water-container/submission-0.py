class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maximumArea = 0
        left, right = 0, len(heights) - 1

        while left < right:
            maximumArea = max(maximumArea, (right - left) * (min(heights[left], heights[right])))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maximumArea
