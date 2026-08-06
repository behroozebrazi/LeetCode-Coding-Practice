# https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        prev = 0

        for letter in s[::-1]:
            curr = roman[letter]

            result += curr if curr >= prev else -curr

            prev = curr

        return result