class Solution:
    def isHappy(self, n: int) -> bool:
        def cycle(n, seen=set()):
            if n == 1:
                return True

            res = 0
            while n > 0:
                n, digit = divmod(n, 10)
                res += (digit * digit)

            if res in seen:
                # cycle
                return False

            seen.add(res)
            return cycle(res, seen)

        return cycle(n)


        