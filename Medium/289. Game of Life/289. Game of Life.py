# https://leetcode.com/problems/game-of-life

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        for r in range(m):
            for c in range(n):
                live = 0

                for i in range(max(0, r - 1), min(m, r + 2)):
                    for j in range(max(0, c - 1), min(n, c + 2)):
                        if (i != r or j != c) and board[i][j] in (1, 2):
                            live += 1

                if board[r][c] == 1 and (live < 2 or live > 3):
                    board[r][c] = 2

                elif board[r][c] == 0 and live == 3:
                    board[r][c] = 3

        for r in range(m):
            for c in range(n):
                board[r][c] %= 2