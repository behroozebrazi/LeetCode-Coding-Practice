# https://leetcode.com/problems/construct-quad-tree

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def build(row, col, size):
            value = grid[row][col]

            # Check if the entire square has the same value
            same = True
            for r in range(row, row + size):
                for c in range(col, col + size):
                    if grid[r][c] != value:
                        same = False
                        break
                if not same:
                    break

            # If all values are the same -> leaf node
            if same:
                return Node(value == 1, True)

            # Divide into 4 parts
            half = size // 2

            topLeft = build(row, col, half)
            topRight = build(row, col + half, half)
            bottomLeft = build(row + half, col, half)
            bottomRight = build(row + half, col + half, half)

            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return build(0, 0, len(grid))