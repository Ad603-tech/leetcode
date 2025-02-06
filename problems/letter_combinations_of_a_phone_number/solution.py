class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {'2' : 'abc',
                  '3' : 'def',
                  '4' : 'ghi',
                  '5' : 'jkl',
                  '6' : 'mno',
                  '7' : 'pqrs',
                  '8' : 'tuv',
                  '9' : 'wxyz'}
        
        combinations = []
        def combo(idx, comb):
            if len(digits) == idx:
                combinations.append(comb)
                return

            for letter in phone[digits[idx]]:
                combo(idx + 1, comb+letter)  
        
        combo(0, "")
        return combinations