class Solution:
    def rob(self, nums: List[int]) -> int:
        previous_two, previous_one = 0, 0
        for money in nums:
            previous_two, previous_one = previous_one, max(previous_one, previous_two + money)
        return previous_one
        