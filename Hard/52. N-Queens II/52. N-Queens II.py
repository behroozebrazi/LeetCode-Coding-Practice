# https://leetcode.com/problems/n-queens-ii

class Solution:
    def totalNQueens(self, n: int) -> int:

        cols = set()
        diagonal1 = set()   # row - col
        diagonal2 = set()   # row + col

        def backtrack(row):
            if row == n:
                return 1

            count = 0

            for col in range(n):
                if col in cols: continue
                if row - col in diagonal1: continue
                if row + col in diagonal2: continue

                # Choose
                cols.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)

                # Explore
                count += backtrack(row + 1)

                # Undo
                cols.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)

            return count

        return backtrack(0)



# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         result = 0
#         cols = set(range(n))
#         diagonal1 = set()
#         diagonal2 = set()

#         def backtrack(row):
#             nonlocal result

#             if row == n:
#                 result += 1
#                 return

#             for col in cols.copy():

#                 if row - col in diagonal1:
#                     continue

#                 if row + col in diagonal2:
#                     continue

#                 # Choose
#                 cols.remove(col)
#                 diagonal1.add(row - col)
#                 diagonal2.add(row + col)

#                 # Explore
#                 backtrack(row + 1)

#                 # Undo
#                 cols.add(col)
#                 diagonal1.remove(row - col)
#                 diagonal2.remove(row + col)

#         backtrack(0)

#         return result