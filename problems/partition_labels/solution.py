class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapping = {}
        for i in range(len(s)):
            mapping[s[i]] = i
        
        prev = -1
        maxi = 0
        res = []

        for i in range(len(s)):
            maxi = max(maxi, mapping[s[i]])
            if maxi == i:
                count = maxi - prev
                res.append(count)
                prev = maxi
        return res