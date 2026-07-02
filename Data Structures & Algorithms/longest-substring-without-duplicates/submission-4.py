class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        runninglength = 0
        hmap = []
        k = 0
        for idx in range(len(s)):
            if s[idx] in hmap:
                k = idx
                hmap = hmap[k:]
            hmap.append(s[idx])
            print(hmap)
            maxlength = max(maxlength, len(hmap))
        return maxlength
        