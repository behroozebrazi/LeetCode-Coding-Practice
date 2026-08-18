# https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sumMax = root.val

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal sumMax

            if not node: return 0

            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)
            sumMax = max(leftMax + node.val + rightMax, sumMax)

            return max(leftMax, rightMax) + node.val

        dfs(root)

        return sumMax