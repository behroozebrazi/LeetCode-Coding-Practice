# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:

        memo = dict()

        def step(remainSteps):
            if remainSteps == 0:
                return 1
            elif remainSteps < 0:
                return 0

            if remainSteps not in memo:
                memo[remainSteps] = step(remainSteps - 1) + step(remainSteps - 2)

            return memo[remainSteps]

        step(n)

        return memo[n]