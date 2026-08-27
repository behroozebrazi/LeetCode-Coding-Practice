# https://leetcode.com/problems/ipo

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        projects = sorted(zip(capital, profits))

        max_profit = []
        i = 0

        for _ in range(k):

            # Add every project we can currently afford
            while i < len(projects) and projects[i][0] <= w:
                heappush(max_profit, -projects[i][1])
                i += 1

            # No affordable project
            if not max_profit:
                break

            # Take the project with maximum profit
            w += -heappop(max_profit)

        return w



# class Solution:
#     def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

#         capitals = []
#         project_profits = []

#         for pro, cap in zip(profits, capital):
#             heappush(project_profits, (- pro, cap))

#         while k > 0 and project_profits:
#             prof, capi = heappop(project_profits)

#             if w >= capi:
#                 w += -prof
#                 k -= 1
#             else:
#                 heappush(capitals, (capi, prof))

#             while capitals:
#                 capi, prof = capitals[0]
#                 if  w >= capi:
#                     heappop(capitals)
#                     heappush(project_profits, (prof, capi))
#                 else:
#                     break        

#         return w