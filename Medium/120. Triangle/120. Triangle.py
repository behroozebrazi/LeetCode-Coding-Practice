# https://leetcode.com/problems/triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):

                triangle[row][col] += min(
                    triangle[row + 1][col],
                    triangle[row + 1][col + 1]
                )

        return triangle[0][0]



# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:

#         for row in range(1, len(triangle)):
#             for col in range(len(triangle[row])):

#                 if col == 0:
#                     triangle[row][col] += triangle[row - 1][col]

#                 elif col == len(triangle[row] - 1):
#                     triangle[row][col] += triangle[row - 1][col - 1]

#                 else:
#                     triangle[row][col] += min(
#                         triangle[row - 1][col - 1], 
#                         triangle[row - 1][col]
#                         )

#         return min(triangle[-1])