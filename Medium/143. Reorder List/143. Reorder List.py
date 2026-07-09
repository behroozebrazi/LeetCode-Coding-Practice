# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not (head and head.next and head.next.next):
            return head

        lst = []
        while head:
            lst.append(head)
            head = head.next
            lst[-1].next = None

        mid = len(lst) // 2
        pointer = ListNode(0, head)

        for i in range(mid):
            pointer.next = lst[i]
            pointer.next.next = lst[-i -1]
            pointer = pointer.next.next

        if len(lst) % 2 != 0:
            pointer.next = lst[mid]