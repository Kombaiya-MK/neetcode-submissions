class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        k = 0
        for space in spaces:
            # if space != k:
            ans.append(s[k:space])
            k = space
        if k != len(s):
            ans.append(s[k:len(s)])
        return " ".join(ans)

        
