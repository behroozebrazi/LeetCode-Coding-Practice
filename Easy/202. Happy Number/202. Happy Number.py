# https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while n > 1:
            seen.add(n)

            sumNum = 0
            while n > 0:
                sumNum += (n % 10) ** 2
                n = n // 10
            n = sumNum

            if n in seen:
                return False

        return True 