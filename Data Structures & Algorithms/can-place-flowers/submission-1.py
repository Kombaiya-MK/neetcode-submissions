class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = 0
        plots = 0

        for idx in range(1, len(flowerbed) - 1):

            prev = flowerbed[idx - 1] == 0
            current = flowerbed[idx] == 0
            nextPlot = flowerbed[idx + 1] == 0

            if prev and current and nextPlot:
                flowers += 1
            
            if flowers == n:
                return True
        return False


        