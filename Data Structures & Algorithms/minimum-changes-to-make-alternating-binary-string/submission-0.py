class Solution:
    def minOperations(self, s: str) -> int:
        ops = 0
        arr = list(s)
        
        for idx in range(1, len(arr)):
            if arr[idx-1] == arr[idx]:
                ops += 1
                
                if arr[idx] == 0:
                    arr[idx] = 1
                else:
                    arr[idx] = 0
        return ops
        