class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        letters1 = list(word1)
        letters2 = list(word2)

        result = []
       
        i = 0
        while i < len(letters1) or i < len(letters2):
            if i < len(letters1):
                result.append(letters1[i])
            if i < len(letters2):
                result.append(letters2[i])
                
            i += 1

        return ''.join(result)
