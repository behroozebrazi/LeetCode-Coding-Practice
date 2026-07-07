# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        sentinel = ListNode(0, head)

        rd = sentinel

        while head:

            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                rd.next = head.next
                
            else:
                rd = rd.next

            head = head.next

        return sentinel.next