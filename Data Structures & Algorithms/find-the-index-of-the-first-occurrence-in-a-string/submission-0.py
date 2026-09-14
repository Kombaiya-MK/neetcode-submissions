class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = 0

        for idx in range(len(haystack)):
            if haystack[idx] == needle[k]:
                k += 1

                if k == len(needle):
                    return idx - k + 1
            else:
                k = 0

        return -1
