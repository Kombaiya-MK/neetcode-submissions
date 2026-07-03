class Solution:
    def trap(self, height: List[int]) -> int:
        maxArea = 0
        n = len(height)
        left, right = 0, n - 1
        leftMax, rightMax = 0, 0
        while left < right:

            if height[left] < height[right]:
                left += 1
                leftMax = max(leftMax, height[left])
                maxArea += (leftMax - height[left])
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                maxArea += (rightMax - height[right])
            
        return maxArea
            