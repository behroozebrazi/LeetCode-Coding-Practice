# https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x

        left = 2
        right = x // 2

        while left <= right:
            mid = (left + right) // 2
            power = mid * mid

            if power < x:
                left = mid + 1
            elif power > x:
                right = mid - 1
            else:
                return mid

        return right