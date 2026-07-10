# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        left = 0
        right = len(nums) - 1
        
        while left <= right and (result[0] == -1 or result[1] == -1):

            if nums[left] == target and result[0] == -1:
                result[0] = left
            if nums[right] == target and result[1] == -1:
                result[1] = right

            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                if nums[left] < target:
                    left += 1
                if target < nums[right]:
                    right -= 1

        return result