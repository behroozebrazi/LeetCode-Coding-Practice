# https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        bfsList = []

        def bfs(node, level):
            if node:
                bfsList.append((node.val, level))
                bfs(node.right, level + 1)
                bfs(node.left, level + 1)

        bfs(root, 0)

        if bfsList:
            currLevel = 0
            for value, level in bfsList:
                if currLevel == level:
                    result.append(value)
                    currLevel += 1

        return result