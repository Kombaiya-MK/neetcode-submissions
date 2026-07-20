class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = 0
        plots = 0

        for val in flowerbed:

            if plots == 3:
                flowers += 1
                plots = 0
            if val == 0:
                plots += 1
            else:
                plots = 0
        return flowers == n


        