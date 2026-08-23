# https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []

        def backtrack(start, current):
            if len(current) == k:
                result.append(current.copy())
                return

            for num in range(start, n + 1):
                current.append(num)
                backtrack(num + 1, current)
                current.pop()

        backtrack(1, [])

        return result