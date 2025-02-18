class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for index, num in enumerate(nums):
            comp = target - num

            if comp in num_index:
                return [num_index[comp], index]
            
            num_index[num] = index
        return []