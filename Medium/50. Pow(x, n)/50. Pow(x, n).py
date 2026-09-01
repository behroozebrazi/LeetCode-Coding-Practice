# https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n > 0:
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        return result



# class Solution:
#     def myPow(self, x: float, n: int) -> float:

#         num = x
#         if n < 0:
#             num = 1 / x
#             n *= -1

#         result = 1
#         powers = dict()
#         degree = 1
#         while degree <= n:
#             powers[degree] = num
#             degree *= 2
#             num *= num

#         degree /= 2
#         while n != 0:
#             if degree <= n:
#                 result *= powers[degree]
#                 n -= degree
#             degree /= 2

#         return result