class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxElement = -1
        ans = [-1] * len(arr)
        for idx in range(len(arr) - 1, -1, -1):
            ans[idx] = maxElement
            maxElement = max(maxElement, arr[idx])
        return ans

        