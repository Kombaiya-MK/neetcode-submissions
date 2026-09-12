class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        cur = s[0]
        ans = romans[cur]
        for r in s[1:]:
            if romans[r] > romans[cur]:
                ans -= romans[cur] * 2
            ans += romans[r]
            cur = r
        return ans