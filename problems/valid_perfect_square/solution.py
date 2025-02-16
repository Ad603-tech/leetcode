class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num

        while left <= right:
            m = (left + right) // 2
            if m * m == num:
                return True
            elif m * m > num:
                right = m - 1
            else:
                left = m + 1
        
        return False