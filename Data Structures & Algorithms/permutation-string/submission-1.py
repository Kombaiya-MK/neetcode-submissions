class Solution:
    def checkInclusion(self, str1: str, str2: str) -> bool:
        hashMap = {}
        window = {}

        for i in str1:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
            
        left = 0

        for right in range(len(str2)):

            if str2[right] in window:
                window[str2[right]] += 1
            else:
                window[str2[right]] = 1

            if right - left + 1 > len(str1):
                window[str2[left]] -= 1
                if window[str2[left]] == 0:
                    del window[str2[left]]
                left += 1

            
            if window == hashMap:
                return True
        return False
        