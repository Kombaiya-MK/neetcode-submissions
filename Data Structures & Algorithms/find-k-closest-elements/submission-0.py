class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        stack = []
        hashMap = {}
        for num in arr:
            hashMap[num] = abs(num-x)
        # print(hashMap)

        sorted_dict = dict(sorted(hashMap.items(), key=lambda kv: kv[1]))
        for num in sorted_dict:
            if k == 0:
                break
            stack.append(num)
            k -= 1
        return sorted(stack)
        
                    
        