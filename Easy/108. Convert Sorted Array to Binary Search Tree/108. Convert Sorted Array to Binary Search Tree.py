# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def divide(left, right):
            if left >= right:
                return None

            mid = (left + right) // 2
            leftNode = divide(left, mid)
            rightNode = divide(mid + 1, right)
            node = TreeNode(nums[mid], leftNode, rightNode)
            return node

        return divide(0, len(nums))



# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

#         def divide(numbers):
#             match len(numbers):
#                 case 0:
#                     return None
#                 case 1:
#                     return TreeNode(numbers[0])
#                 case _:
#                     n = len(numbers) // 2
#                     left = divide(numbers[:n])
#                     right = divide(numbers[n+1:])
#                     node = TreeNode(numbers[n], left, right)
#                     return node

#         return divide(nums)