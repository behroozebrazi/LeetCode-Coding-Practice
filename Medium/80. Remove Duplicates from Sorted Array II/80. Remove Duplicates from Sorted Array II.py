# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return len(nums)

        left = 1
        right = 2

        while right < len(nums):

            if nums[left - 1] != nums[right] or nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]

            right += 1

        return left + 1


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:

#         if len(nums) < 3:
#             return len(nums)

#         left = 1
#         right = 2

#         while right < len(nums):

#             if nums[left - 1] == nums[right] and nums[left] == nums[right]:
#                 right += 1
#             else:
#                 left += 1
#                 nums[left] = nums[right]
#                 right += 1

#         return left + 1