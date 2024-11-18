class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0

        if x < 0:
            return False
        
        y = x
        while y > 0:
            ld = y % 10
            rev = (rev * 10) + ld
            y = y // 10
        
        return x == rev
        
        