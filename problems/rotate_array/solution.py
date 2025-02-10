class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        k = k % n
        if k == 0:
            return
        temp = nums[-k:]
        for i in range(n - 1, -1, -1):
            nums[i] = nums[i - k]
        
        nums[:k] = temp
        print(nums)

        