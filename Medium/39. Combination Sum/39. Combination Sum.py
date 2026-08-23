# https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrack(start, current, total):

            if target < total:
                return

            if target == total:
                result.append(current.copy())
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                current.append(num)
                backtrack(i, current, total + num)
                current.pop()

        backtrack(0, [], 0)

        return result



# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

#         result = set()
#         min_num = min(candidates)
#         max_length = target // min_num

#         def backtrack(current, sum_num):
#             if max_length < len(current) or target < sum_num:
#                 return
#             if sum_num == target:
#                 result.add(tuple(sorted(current)))
#                 return

#             for num in candidates:
#                 current.append(num)
#                 backtrack(current, sum_num + num)
#                 current.pop()

#         backtrack([], 0)

#         return list(result)