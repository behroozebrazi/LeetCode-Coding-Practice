# https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        leafSum = 0
        stack = [(root, "")]

        while stack:
            node, nodeSum = stack.pop()

            nodeSum += str(node.val)

            if not node.left and not node.right:
                leafSum += int(nodeSum)

            if node.left:
                stack.append((node.left, nodeSum))
            if node.right:
                stack.append((node.right, nodeSum))

        return leafSum