# https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:

        result = 0

        for _ in range(32):
            result += n & 1
            n = n >> 1

        return result