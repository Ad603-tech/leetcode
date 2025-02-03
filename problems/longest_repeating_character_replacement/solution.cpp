class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int>char_freq;
        int res = 0;
        int i = 0;
        int max_freq = 0;

        for(int j = 0; j < s.size(); j++) {
            char_freq[s[j]]++;
            max_freq = max(max_freq, char_freq[s[j]]);
            int cur_len = j - i + 1;
            if(cur_len - max_freq > k) {
                char_freq[s[i]]--;
                i++;
            }
            res = max(res, j - i + 1);
        }
        return res;
    }
};