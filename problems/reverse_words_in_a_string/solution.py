class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()
        
        n = len(words) -  1
        result = []

        for i in range(n + 1):
            word = words[n - i]
            result.append(word)

        reverse_word = ' '.join(result)
        return reverse_word
