class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap =  {}

        for idx in range(len(nums)):
            if nums[idx] in hashMap:
                diff = idx - hashMap[nums[idx]]
                if diff <= k:
                    return True
            else:
                hashMap[nums[idx]] = idx
        return False        