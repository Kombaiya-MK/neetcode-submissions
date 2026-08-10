class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitStr = []
        for ch in s.split(" "):
            if ch != "":
                splitStr.append(ch)
        print(splitStr)
        return len(splitStr[-1])
        