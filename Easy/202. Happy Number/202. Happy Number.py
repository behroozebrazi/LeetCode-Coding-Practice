# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        noRepeatNum = set()

        while n > 1:
            noRepeatNum.add(n)

            sum = 0
            while n > 0:
                sum += (n % 10) ** 2
                n = n // 10
            n = sum

            if sum in noRepeatNum:
                return False
                
        return True 