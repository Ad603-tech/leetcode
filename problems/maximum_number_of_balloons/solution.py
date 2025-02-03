class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_count = Counter(text)

        balloon_count = {
            'b' : 1,
            'a' : 1,
            'l' : 2,
            'o' : 2,
            'n' : 1
        }

        max_instances = float('inf')
        for char, req in balloon_count.items():
            if char in char_count:
                max_instances = min(max_instances, char_count[char] // req)
            else:
                return 0
        
        return max_instances