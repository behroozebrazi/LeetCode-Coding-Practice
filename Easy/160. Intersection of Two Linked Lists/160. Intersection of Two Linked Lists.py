# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        unique = set()

        while headA:
            unique.add(headA)
            headA = headA.next

        while headB and not headB in unique:
            headB = headB.next
        
        if headB:
            return headB
        else:
            return None