# https://leetcode.com/problems/surrounded-regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        def dfs(row, col):
            if 0 <= row and row < rows and 0 <= col and col < cols and board[row][col] == "O":
                board[row][col] = "B"
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)

        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                match board[row][col]:
                    case "O":
                        board[row][col] = "X"
                    case "B":
                        board[row][col] = "O"