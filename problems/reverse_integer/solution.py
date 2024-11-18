class Solution:
    def reverse(self, x: int) -> int:
        revNum = 0
        y = abs(x)

        while y > 0:
            ld = y % 10
            revNum = (revNum * 10) + ld
            y = y // 10
        
        if revNum > 2 ** 31 - 1 or revNum < -2 ** 31:
            return 0
        if x < 0:
            return -revNum
        
        return revNum
        