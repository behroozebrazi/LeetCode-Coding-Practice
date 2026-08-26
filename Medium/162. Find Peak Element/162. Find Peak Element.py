# https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                # We are on the descending side.
                # mid could be a peak.
                right = mid
            else:
                # We are on the ascending side.
                # A peak must exist to the right.
                left = mid + 1

        return left
        # return right