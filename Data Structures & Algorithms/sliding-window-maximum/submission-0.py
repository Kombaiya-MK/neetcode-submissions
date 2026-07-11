from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dq = deque()
        left = 0
        for right in range(len(nums)):
            while dq and nums[right] > nums[dq[-1]]:
                dq.pop()
            dq.append(right)

            if right - left + 1 > k:
                if dq[0] == left:
                    dq.popleft()
                left += 1
            if right - left + 1 == k:
                ans.append(nums[dq[0]])
        return ans
        