# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode()
        curr = result
        parity = 0

        while l1 and l2:
            parity = l1.val + l2.val + parity                                     
            val = parity % 10
            parity = parity // 10
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        rest = l1 if l1 else l2
        while rest:
            parity = rest.val + parity                                     
            val = parity % 10
            parity = parity // 10
            curr.next = ListNode(val)
            curr = curr.next
            rest = rest.next

        if parity > 0:
            curr.next = ListNode(parity)

        return result.next