class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = []
        if x < 0:
            return False
        while x > 0:
            rem = x % 10
            arr.append(rem)
            x = x // 10
        
        left, right = 0, len(arr) - 1

        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True
        