class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0 , len(s) - 1
        k = 0

        while left < right:
            print(k)
            if s[left] != s[right]:
                if k == 1:
                    return False
                elif left + 1 < len(s) - 1 and s[left + 1] == s[right]:
                    left += 1
                    k += 1
                elif right - 1 > -1 and s[right - 1] == s[left]:
                    right -= 1
                    k += 1
                else:
                    return False
            left += 1
            right -= 1
        return True