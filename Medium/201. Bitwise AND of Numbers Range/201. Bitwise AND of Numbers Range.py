# https://leetcode.com/problems/bitwise-and-of-numbers-range

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        # find common prefix
        while left < right:
            right = right & (right - 1)

        return right



# class Solution:
#     def rangeBitwiseAnd(self, left: int, right: int) -> int:

#         shift = 0

#         # find common prefix
#         while left != right:
#             left >>= 1
#             right >>= 1
#             shift += 1

#         return left << shift