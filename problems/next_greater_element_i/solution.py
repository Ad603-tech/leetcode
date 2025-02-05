class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        result = []

        for num in reversed(nums2):
            while stack:
                if stack[-1] > num:
                    next_greater[num] = stack[-1]
                    stack.append(num)
                    break
                else:
                    stack.pop()
            if not stack:
                next_greater[num] = -1
                stack.append(num)
        
        for n in nums1:
            result.append(next_greater[n])
        
        return result


