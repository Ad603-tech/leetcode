class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_ind_s = {}
        char_ind_t = {}

        for i in range(len(s)):
            if s[i] not in char_ind_s:
                char_ind_s[s[i]] = i
            if t[i] not in char_ind_t:
                char_ind_t[t[i]] = i
            if char_ind_s[s[i]] != char_ind_t[t[i]]:
                return False
        
        return True
        
        