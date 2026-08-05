# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 1
        maxReach = 0
        nextMaxReach = nums[0]
        lastIndex = len(nums) - 1

        for i in range(1, len(nums)):

            if nextMaxReach < i:
                return 0

            if lastIndex <= nextMaxReach:
                return jumps

            if maxReach < i:
                maxReach = nextMaxReach
                jumps += 1

            nextMaxReach = max(nextMaxReach, nums[i] + i)

        return 0