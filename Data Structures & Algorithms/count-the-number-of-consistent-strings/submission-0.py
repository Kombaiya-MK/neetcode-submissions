class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            count = 0
            for ch in word:
                if ch in allowed:
                    count += 1
            if count == len(word):
                ans += 1
        return ans
        