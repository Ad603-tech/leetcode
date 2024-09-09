class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        
        for char, word in zip(pattern, s):
            if char in mapping:
                if mapping[char] != hash(word):
                    return False
            else:
                mapping[char] = hash(word)
                
        return len(set(mapping.keys())) == len(set(mapping.values()))