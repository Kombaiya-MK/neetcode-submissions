class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        for idx in range(len(flowerbed)):

            prev = flowerbed[idx - 1] == 0 if (idx - 1) >= 0 else True
            current = flowerbed[idx] == 0 
            nextPlot = flowerbed[idx + 1] == 0 if (idx + 1) < len(flowerbed) else True

            if prev and current and nextPlot:
                n -= 1
                flowerbed[idx] = 1
                if n == 0:
                    return True
        return False


        