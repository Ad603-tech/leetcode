class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_occ(nums, target):
            n = len(nums)
            low = 0
            high = n - 1
            fo = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    fo = mid
                    high = mid - 1
                elif target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
                
            return fo
        
        def last_occ(nums, target):
            n = len(nums)
            low = 0
            high = n - 1
            lo = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    lo = mid
                    low = mid + 1
                elif target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return lo
        
        fo = first_occ(nums, target)
        lo = last_occ(nums, target)
        return [fo, lo]

                
