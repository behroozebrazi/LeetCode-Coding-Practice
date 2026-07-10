# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) <= 1 or nums[0] < nums[-1]:
            return self.searchInsert(nums, target)

        left, mid, right = 0, 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid - 1] > nums[mid]:
                break
            if nums[mid] > nums[mid + 1]:
                mid += 1
                break
            if nums[mid] < nums[left]:
                right = mid
            if nums[mid] > nums[right]:
                left = mid

        second_part = nums[mid] <= target and target <= nums[-1]

        if second_part:
            position = self.searchInsert(nums[mid:], target)
        else:
            position = self.searchInsert(nums[:mid], target)
        if position >= 0 and second_part:
            position += mid
            
        return position
        
    def searchInsert(self, nums: List[int], target: int):
        left, mid, right = 0, 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1