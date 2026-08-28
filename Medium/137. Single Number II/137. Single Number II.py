# https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0
        one = 1

        for _ in range(32):
            total_ones = 0

            for num in nums:
                if num & one != 0:
                    total_ones += 1

            if total_ones % 3 == 1:
                result = result | one

            one = one << 1

        return result - 2 ** 32 if result >= 2 ** 31 else result



# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:

#         ones = 0
#         twos = 0

#         for num in nums:
#             ones = (ones ^ num) & ~twos
#             twos = (twos ^ num) & ~ones

#         return ones