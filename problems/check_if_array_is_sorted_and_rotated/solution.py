class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums=sorted(nums)
        for k in range(len(nums)):
            if nums[k:]+nums[:k] == sorted_nums:
                return True
        return False
    
