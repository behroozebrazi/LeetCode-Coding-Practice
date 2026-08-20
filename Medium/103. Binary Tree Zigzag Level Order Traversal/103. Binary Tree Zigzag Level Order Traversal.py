# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        queue = deque()

        if root:
            queue.append(root)
        
        while queue:
            level_size = len(queue)
            level_nums = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nums.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if len(result) % 2 == 1:
                level_nums.reverse()

            result.append(level_nums)

        return result