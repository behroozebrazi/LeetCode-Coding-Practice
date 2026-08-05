# https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left = right = 0

        while right < len(nums):

            while right < len(nums) and nums[right] == val:
                right += 1

            if right < len(nums):
                nums[left] = nums[right]
                left += 1
                right += 1

        return left