class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        i = 0
        for i in candies:
            candy = i + extraCandies
            if candy >= max(candies):
                result.append(True)
            else:
                result.append(False)
            i += 1

        return result
        