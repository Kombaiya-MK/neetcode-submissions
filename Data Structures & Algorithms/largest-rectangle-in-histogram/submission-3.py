class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = heights[0]
        stack = []
        heights.append(0)
        for idx in range(len(heights)):

            while stack and heights[stack[-1]] > heights[idx]:
                val = stack.pop()
                left = stack[-1] if stack else -1
                width = idx - left - 1
                print(val, width)
                maxArea = max(maxArea, width * heights[val])
            stack.append(idx)
            # maxArea = max(maxArea, (len(stack)) * stack[-1])

        # print(stack)
        return maxArea
        