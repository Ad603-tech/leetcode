class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g)
        m = len(s)
        g.sort()
        s.sort()
        l = 0
        r = 0
        while l < n and r < m:
            if g[l] <= s[r]:
                l += 1
            r += 1

        return l