class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findfirst(nums, target):
            low = 0
            high = len(nums) - 1
            first_pos = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    first_pos = mid
                    high = mid - 1

                elif nums[mid] < target:
                    low = mid + 1
            
                else:
                    high = mid - 1
            return first_pos

        def findlast(nums, target):
            low = 0
            high = len(nums) - 1
            last_pos = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last_pos = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
            
                else:
                    high = mid - 1
            return last_pos

        first_occ = findfirst(nums, target)
        last_occ = findlast(nums, target)

        return [first_occ, last_occ]