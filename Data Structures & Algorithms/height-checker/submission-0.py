class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        ans = 0

        for idx in range(len(heights)):
            if expected[idx] != heights[idx]:
                ans += 1
        return ans
        