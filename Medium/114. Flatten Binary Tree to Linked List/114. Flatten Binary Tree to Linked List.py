# https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        tail = None

        def dfs(node):
            nonlocal tail

            if node:
                dfs(node.right)
                dfs(node.left)

                node.right = tail
                node.left = None
                tail = node

        dfs(root)