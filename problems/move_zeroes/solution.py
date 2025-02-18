class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1
        for right in range(len(nums)):
            if nums[right] == 0:
                left = right
                break

        if len(nums) == 1:
            return nums
        if left == -1:
            return nums
            
        for right in range(left + 1, len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        return nums
        