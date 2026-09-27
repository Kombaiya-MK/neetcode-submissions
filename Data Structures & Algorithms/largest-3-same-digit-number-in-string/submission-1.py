class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if len(num) <= 0:
            return ""
        maxNum = -1
        curlen = 0
        curNum = num[0]
        for digit in num:

            if curNum == digit:
                curlen += 1

            else:
                curNum = digit
                curlen = 1

            if curlen == 3:
                maxNum = max(maxNum, int(curNum))
                curlen = 1
                
        if maxNum == -1:
            return ""
        return str(maxNum)*3