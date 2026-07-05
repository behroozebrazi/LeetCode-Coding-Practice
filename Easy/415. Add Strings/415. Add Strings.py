# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        carry = 0
        sumNum = ''
        while carry != 0 or (n1 != 0 and n2 != 0):
            digit1, digit2 = 0, 0
            if n1 > 0:
                n1 -= 1
                digit1 = int(num1[n1])
            if n2 > 0:
                n2 -= 1
                digit2 = int(num2[n2])
            temp = digit1 + digit2 + carry
            if temp > 9:
                temp -= 10
                carry = 1
            else:
                carry = 0
            sumNum = str(temp) + sumNum
        sumNum = num1[:n1] + sumNum if n1 > n2 else num2[:n2] + sumNum
        return sumNum