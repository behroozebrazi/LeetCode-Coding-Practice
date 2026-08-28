# https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        digit = len(digits)

        while carry == 1 and digit > 0:
            digit -= 1
            carry, mod = divmod(digits[digit] + carry, 10)
            digits[digit] = mod

        if carry != 0:
            digits.insert(0, carry)

        return digits