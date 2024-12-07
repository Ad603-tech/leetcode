class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
         # Bottom-Up function for the linear house robber problem
        def rob_linear(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]

        # Rob houses excluding the first or excluding the last
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))