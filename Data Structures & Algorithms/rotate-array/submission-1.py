class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n == 0 or k % n == 0:
            return nums
        self.reverseArray(nums, 0, n - 1)
        print(nums)
        self.reverseArray(nums, 0, k - 1)
        print(nums)
        self.reverseArray(nums, k, n - 1)



    def reverseArray(self, arr, left, right):

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        