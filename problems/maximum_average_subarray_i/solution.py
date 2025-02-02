class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
        max_sum = curr_sum = sum(nums[:k])
        
        for i in range(k, n):
            curr_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, curr_sum)
        
        max_avg = max_sum / k

        return max_avg