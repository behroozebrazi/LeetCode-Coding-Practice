# https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        maxReach = 0
        lastIndex = len(nums) - 1

        for i, num in enumerate(nums):
            if i <= maxReach:
                maxReach = max(maxReach, num + i)
                if lastIndex <= maxReach:
                    return True
            else:
                break

        return False


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:

#         maxReach = 0
#         lastIndex = len(nums) - 1

#         for i, num in enumerate(nums):
#             if maxReach < i:
#                 return False

#             maxReach = max(maxReach, num + i)

#             if lastIndex <= maxReach:
#                 return True

#         return True