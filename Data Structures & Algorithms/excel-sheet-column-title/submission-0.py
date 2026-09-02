class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []

        while columnNumber > 0:
            rem = columnNumber % 26
            print(rem)
            ans.append(chr(rem + 64))
            columnNumber //= 26
        print(ans)
        return "".join(reversed(ans))