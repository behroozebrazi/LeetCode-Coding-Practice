# https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(current, digits):
            if len(digits) == 0:
                result.append(current.copy())
                return

            for i in range(len(digits)):
                new_nums = digits[:i] + digits[i+1:]
                current.append(digits[i])
                backtrack(current, new_nums)
                current.pop()

        backtrack([], nums)

        return result