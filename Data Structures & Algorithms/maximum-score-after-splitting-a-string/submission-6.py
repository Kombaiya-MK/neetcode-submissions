class Solution:
    def maxScore(self, s: str) -> int:
        totalSum = 0

        for ch in s:
            totalSum += int(ch)

        zeros = 0
        ones = 0
        maxSum = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1

            maxSum = max(maxSum, totalSum + zeros - ones)

        return maxSum