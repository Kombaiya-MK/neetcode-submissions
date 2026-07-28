class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pairs = []

        for num in arr:
            pairs.append((abs(num-x), num))

        pairs.sort()

        answer = []

        for i in range(k):
            answer.append(pairs[i][1])

        answer.sort()
        return answer