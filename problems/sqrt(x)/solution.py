class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            m = (left + right) // 2
            square = m * m
            if square == x:
                return m
            elif square > x:
                right = m - 1
            else:
                left = m + 1
        return right