# https://leetcode.com/problems/snakes-and-ladders

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        rows, cols = len(board), len(board[0])
        target = rows * cols
        queue = deque([(1, 0)])
        visited = set([1])

        def get_position(square):
            # Convert square number -> board[row][col]
            square -= 1
            row_from_bottom = square // cols
            col = square % rows
            row = rows - row_from_bottom - 1
            # Every other row is reversed
            if row_from_bottom % 2 == 1:
                col = cols - col - 1
            return row, col

        while queue:
            cell, moves = queue.popleft()

            for dice in range(1, 7):
                next_square = cell + dice

                if next_square > target:
                    break

                row, col = get_position(next_square)
                steps = board[row][col]

                if steps != -1:
                    next_square = steps

                if next_square == target:
                    return moves + 1

                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1