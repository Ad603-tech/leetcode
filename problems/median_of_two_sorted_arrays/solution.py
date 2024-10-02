class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2

        left, right = 0, m
        while left < right:
            i = (left + right) // 2
            j = total_left - i

            if nums1[i] < nums2[j-1]:
                left = i + 1
            else:
                right = i

        i = left
        j = total_left - i

        nums1LeftMax = float('-inf') if i == 0 else nums1[i-1]
        nums2LeftMax = float('-inf') if j == 0 else nums2[j-1]
        nums1RightMin = float('inf') if i == m else nums1[i]
        nums2RightMin = float('inf') if j == n else nums2[j]

        if (m+n) % 2 == 1:
            return max(nums1LeftMax, nums2LeftMax)
        else:
            return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2.0
