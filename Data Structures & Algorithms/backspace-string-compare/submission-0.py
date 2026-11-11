class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans1 = []
        ans2 = []
        for ch in s:
            if len(ans1) > 0 and ch == '#':
                ans1.pop()
            else:
                ans1.append(ch)
        for ch in t:
            if len(ans2) > 0 and ch == '#':
                ans2.pop()
            else:
                ans2.append(ch)
        
        if len(ans1) != len(ans2):
            return False

        for idx in range(len(ans1)):
            if ans1[idx] != ans2[idx]:
                return False
        return True
        

