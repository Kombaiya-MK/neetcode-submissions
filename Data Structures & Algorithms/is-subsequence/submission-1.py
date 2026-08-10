class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        count = 0
        for ch in s:
            if ch not in t:
                return False
        return True
        