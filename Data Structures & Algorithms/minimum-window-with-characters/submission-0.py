from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)

        window = {}

        required = len(need)     
        formed = 0               

        left = 0

        minLength = float("inf")
        startIndex = 0

        for right in range(len(s)):
            ch = s[right]

            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:

                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    startIndex = left

                leftChar = s[left]
                window[leftChar] -= 1

                if leftChar in need and window[leftChar] < need[leftChar]:
                    formed -= 1

                left += 1

        if minLength == float("inf"):
            return ""

        return s[startIndex:startIndex + minLength]