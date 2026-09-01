# https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        nums.append(0)

        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])

        return nums[-1]