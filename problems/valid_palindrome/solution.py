class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''.join(char.lower() for char in s if char.isalnum())
        return self.helper(t, 0, len(t)-1)

    def helper(self, t, start, end):
        if start >= end:
            return True
        if t[start] != t[end]:
            return False
        return self.helper(t, start+1, end-1)