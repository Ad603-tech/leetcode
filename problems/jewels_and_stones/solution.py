class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # count = {}
        # aux = 0
        # for letter in stones:
        #     count[letter] = count.get(letter, 0) + 1
        
        # for jewel in jewels:
        #     aux += count.get(jewel, 0)
        
        # return aux

        jewel_count = 0
        for stone in stones:
            if stone in jewels:
                jewel_count += 1
        
        return jewel_count