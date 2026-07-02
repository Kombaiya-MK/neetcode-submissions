class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        runninglength = 0
        hmap = {}
        for i in s:
            if i in hmap:
                runninglength = 0
                hmap = {}
            runninglength += 1
            hmap[i] = 1
            maxlength = max(maxlength, runninglength)
        return maxlength
        