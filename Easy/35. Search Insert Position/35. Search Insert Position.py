# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if target < nums[mid]:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
            
        return left