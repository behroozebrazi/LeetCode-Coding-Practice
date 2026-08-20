# https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        def treeTraversal(node, level):
            if not node:
                return

            if len(levels) > level:
                levels[level].append(node.val)
            else:
                levels.append([node.val])

            level += 1
            treeTraversal(node.left, level)
            treeTraversal(node.right, level)

        treeTraversal(root, 0)

        return levels