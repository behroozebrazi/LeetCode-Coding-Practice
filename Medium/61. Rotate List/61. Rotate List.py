# https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        nodeNumbers = 1
        startNode = head
        endNode = head

        while endNode.next:
            nodeNumbers += 1
            endNode = endNode.next

        k = k % nodeNumbers
        if k == 0:
            return head

        endNode.next = startNode
        endNode = startNode

        for _ in range(nodeNumbers - k - 1):
            endNode = endNode.next

        startNode = endNode.next
        endNode.next = None

        return startNode