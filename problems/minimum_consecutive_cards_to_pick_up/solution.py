class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_map = {}
        min_length = float('inf')

        for i in range(len(cards)):
            if cards[i] in card_map:
                min_length = min(min_length, i - card_map[cards[i]] + 1)
            card_map[cards[i]] = i
        
        if min_length != float("inf"):
            return min_length
        else:
            return -1