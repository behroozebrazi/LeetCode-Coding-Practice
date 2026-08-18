# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # Map each value to its index in inorder
        inorder_index = { value: i for i, value in enumerate(inorder) }
        postorder_index = len(postorder) - 1

        def build(left, right):
            nonlocal postorder_index

            # No elements in this subtree
            if left > right:
                return None

            # Last element in postorder is the root
            root_value = postorder[postorder_index]
            postorder_index -= 1

            root = TreeNode(root_value)

            # Find root position in inorder
            mid = inorder_index[root_value]

            # IMPORTANT:
            # Build RIGHT first because we are traversing
            # postorder backwards: Root -> Right -> Left
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)