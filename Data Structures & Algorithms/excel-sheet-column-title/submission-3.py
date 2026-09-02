class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            columnNumber = columnNumber - 1
            rem = columnNumber % 26
            # print(rem)
            ans.append(chr(rem + ord('A')))
            columnNumber //= 26
        # print(ans)
        return "".join(reversed(ans))