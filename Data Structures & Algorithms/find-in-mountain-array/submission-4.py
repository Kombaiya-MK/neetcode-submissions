class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        def binarySearch(left, right, ascending):
            while left <= right:
                mid = left + (right - left) // 2
                val = mountainArr.get(mid)

                if val == target:
                    return mid

                if ascending:
                    if target < val:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if target < val:
                        left = mid + 1
                    else:
                        right = mid - 1

            return -1

        left, right = 0, mountainArr.length() - 1

        while left < right:
            mid = left + (right - left) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left

        ans = binarySearch(0, peak, True)

        if ans != -1:
            return ans

        return binarySearch(peak + 1, mountainArr.length() - 1, False)