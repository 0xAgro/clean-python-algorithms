def myPow(self, x: float, n: int) -> float:
        res = 1

        while n > 0:
            if n & 1:
                res *= x
            x *= x
            n >>= 1

        return res
