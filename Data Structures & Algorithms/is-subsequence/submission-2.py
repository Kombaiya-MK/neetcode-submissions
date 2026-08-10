class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        k = 0
        for idx in range(len(t)):
            if t[idx] == s[k]:
                k += 1
        print(k)
        return k == len(s)