class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        k = 0
        for idx in range(len(t)):
            if t[idx] == s[k]:
                k += 1
        print(k)
        return k == len(s)