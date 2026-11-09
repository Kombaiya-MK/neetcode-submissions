class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        # ids = {}
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            nums = []
            # print(i, j)
            if nums1[i][0] == nums2[j][0]:
                nums.append(nums1[i][0])
                nums.append(nums1[i][1] + nums2[j][1])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                nums.append(nums1[i][0])
                nums.append(nums1[i][1])
                i += 1
            else:
                nums.append(nums2[j][0])
                nums.append(nums2[j][1])
                j += 1
            ans.append(nums)
            
        nums = []
        while i < len(nums1):
            nums.append(nums1[i][0])
            nums.append(nums1[i][1])
            i += 1
            
        while j < len(nums2):
            nums.append(nums2[j][0])
            nums.append(nums2[j][1])
            j += 1
        if len(nums) > 0:
            ans.append(nums)
        return ans
            