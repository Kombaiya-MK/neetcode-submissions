class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        swap = 0
        left_pointer, right_pointer = 0, 0
        while right_pointer < len(nums):
            if nums[right_pointer] != val:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                left_pointer += 1
                swap += 1
            right_pointer += 1
        return swap
        