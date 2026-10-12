from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = Counter(words[0])
        ans = []

        for word in words[1:]:
            common &= Counter(word)

        for ch, count in common.items():
            ans.extend([ch] * count)

        return ans