# https://leetcode.com/problems/average-of-levels-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        queue = deque([root])
        result = []

        while queue:
            level_sum = 0
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level_sum / level_size)

        return result



# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

#         result = []
#         sums = []
#         nums = []

#         def bfs(node, level):
#             if node == None: return

#             if len(sums) == level:
#                 sums.append(node.val)
#                 nums.append(1)
#             else:
#                 sums[level] += node.val
#                 nums[level] += 1

#             level += 1
#             bfs(node.left, level)
#             bfs(node.right, level)

#         bfs(root, 0)

#         for total, num in zip(sums, nums):
#             result.append(total / num)

#         return result