# https://leetcode.com/problems/factorial-trailing-zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:

        counter = 0

        while n >= 5:
            n = n // 5
            counter += n

        return counter



# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         if n <= 1:
#             return 0

#         result = 0
#         counter = {2: 0, 5: 0}

#         for i in range(2, n + 1):

#             div, mod = divmod(i, 2)
#             while mod == 0:
#                 counter[2] += 1
#                 div, mod = divmod(div, 2)

#             div, mod = divmod(i, 5)
#             while mod == 0:
#                 counter[5] += 1
#                 div, mod = divmod(div, 5)

#         result = min(counter[2], counter[5])

#         return result