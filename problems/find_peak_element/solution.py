class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_element = max(nums)
        
        return nums.index(max_element)