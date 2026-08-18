# https://leetcode.com/problems/partition-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        smallerNodes = ListNode(0)
        greaterNodes = ListNode(0)
        smallerTail = smallerNodes
        greaterTail = greaterNodes

        while head:
            if head.val < x:
                smallerTail.next = head
                smallerTail = smallerTail.next
            else:
                greaterTail.next = head
                greaterTail = greaterTail.next
            head = head.next

        greaterTail.next = None
        smallerTail.next = greaterNodes.next

        return smallerNodes.next