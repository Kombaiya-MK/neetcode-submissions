class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        isIncreasing = True
        maxlength = 1
        curlength = 1
        curNum = nums[0]
        for num in nums[1:]:

            if isIncreasing and num > curNum:
                curlength += 1

            elif not isIncreasing and num > curNum:
                curlength = 2
                isIncreasing = True

            elif isIncreasing and num < curNum:
                curlength = 2
                isIncreasing = False

            elif not isIncreasing and num < curNum:
                curlength += 1

            else:
                curlength = 1

            curNum = num
            maxlength = max(maxlength, curlength)

        return maxlength