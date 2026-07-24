class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            currArea = heights[i]
            for j in range(i+1, len(heights)):
                currArea = min(currArea, heights[j])
            maxArea = max(maxArea, currArea * (j - i + 1))
        return maxArea
        