class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0

        length = 0
        for char in reversed(s.strip()):
            if char == ' ':
                break
            length += 1

        return length