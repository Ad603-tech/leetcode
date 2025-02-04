class Solution:
    def isValid(self, s: str) -> bool:
        brac_map = { ')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in brac_map.values():
                stack.append(char)
            elif char in brac_map.keys():
                if not stack or brac_map[char] != stack.pop():
                    return False
        
        return not stack