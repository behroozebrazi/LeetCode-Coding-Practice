# https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def travelTree(node1, node2):
            if not node1 and not node2:
                return True

            elif (node1 and not node2) or (not node1 and node2) or node1.val != node2.val:
                return False

            return travelTree(node1.left, node2.left) and travelTree(node1.right, node2.right)

        return travelTree(p, q)