# https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return len(nums)

        left = 0

        for right in range(1, len(nums)):

            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]

        return left + 1


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:

#         if len(nums) < 2:
#             return len(nums)

#         left = 0
#         right = 1

#         while right < len(nums):

#             if nums[left] != nums[right]:
#                 left += 1
#                 nums[left] = nums[right]

#             right += 1

#         return left + 1