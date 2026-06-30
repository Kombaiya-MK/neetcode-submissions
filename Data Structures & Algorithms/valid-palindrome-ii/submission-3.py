class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0 , len(s) - 1
        k = 0

        def isPalindrome(left, right):
            # if left - right < 2:
            #     return True
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        while left < right:
            if s[left] != s[right]:
                if not isPalindrome(left + 1, right) and not isPalindrome(left, right - 1):
                    return False
            left += 1
            right -= 1
        return True