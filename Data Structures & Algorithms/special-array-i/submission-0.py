class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        isOdd = nums[0] % 2 == 1
        n = len(nums)
        if n <= 1:
            return True
        cur = nums[0]
        for idx in range(1, n):
            runIsOdd = nums[idx] % 2 == 1
            print(isOdd, runIsOdd)
            if isOdd and runIsOdd:
                return False
            elif not isOdd and not runIsOdd:
                return False
            isOdd = runIsOdd
        return True

        