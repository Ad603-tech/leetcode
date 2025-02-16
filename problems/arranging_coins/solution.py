class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            m = (left + right) // 2
            t = m * (m + 1) / 2

            if t == n:
                return m
            elif t < n:
                left = m + 1
            else:
                right = m - 1
        
        return right