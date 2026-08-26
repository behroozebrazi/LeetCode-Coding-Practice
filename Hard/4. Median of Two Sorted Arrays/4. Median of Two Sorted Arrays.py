# https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Always binary-search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:

            # Partition nums1
            partition1 = (left + right) // 2

            # Partition nums2 so left side has half of all elements
            partition2 = (m + n + 1) // 2 - partition1

            # Boundary values
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:

                # Odd total length
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)

                # Even total length
                return (
                    max(maxLeft1, maxLeft2)
                    + min(minRight1, minRight2)
                ) / 2

            # partition1 is too far right
            elif maxLeft1 > minRight2:
                right = partition1 - 1

            # partition1 is too far left
            else:
                left = partition1 + 1