class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def binarySearch(left, right, ascending):
            while left <= right:

                mid = left + (right - left) // 2
                val = mountainArr.get(mid)
                # leftVal = mountainArr.get(left)
                # rightVal = mountainArr.get(right)
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
            val = mountainArr.get(mid)
            nextVal = mountainArr.get(mid + 1)
            if val == target:
                return mid
            
            if val < nextVal:
                left = mid + 1

            else:
                right = mid
        ans = binarySearch(0, left, True)

        if ans == -1:
            ans = binarySearch(left + 1, mountainArr.length() - 1, False)
        
        return ans