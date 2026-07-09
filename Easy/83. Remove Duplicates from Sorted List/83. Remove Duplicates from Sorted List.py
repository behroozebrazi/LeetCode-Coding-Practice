# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        uniqueNodes = set()
        sentinel = ListNode(0, head)
        pointer = sentinel

        while pointer.next:
            if pointer.next.val in uniqueNodes:
                pointer.next = pointer.next.next
            else:
                uniqueNodes.add(pointer.next.val)
                pointer = pointer.next

        return sentinel.next