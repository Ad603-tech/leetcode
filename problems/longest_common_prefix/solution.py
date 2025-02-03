class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        v = sorted(strs)
        str1 = v[0]
        str2 = v[-1]

        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                return ans
            ans += str1[i]
        
        return ans