class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, maxLength, zeroCount = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            if zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength