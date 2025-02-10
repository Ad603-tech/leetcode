class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = {}
        count = 0

        for i in range(len(nums)):
            if nums[i] in pairs:
                count += pairs[nums[i]]
                pairs[nums[i]] += 1
            else:
                pairs[nums[i]] = 1
        
        return count