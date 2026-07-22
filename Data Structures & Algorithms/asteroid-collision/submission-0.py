class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            isAlive = True
            while isAlive and stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()

                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    isAlive = False
                else:
                    isAlive = False
                # break
            if isAlive:
                stack.append(asteroid)
            # print(stack)
        return stack