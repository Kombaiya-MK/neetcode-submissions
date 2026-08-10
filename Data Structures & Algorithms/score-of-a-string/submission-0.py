class Solution:
    def scoreOfString(self, s: str) -> int:
        adjChr = s[0]
        score = 0
        for idx in range(1, len(s)):

            score += abs(ord(adjChr) - ord(s[idx]))
            adjChr = s[idx]
        return score        