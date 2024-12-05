class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        minPrice = float('inf')

        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            max_pro = max(max_pro, prices[i] - minPrice)
        
        return max_pro
        