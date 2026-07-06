# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head

        nxt = head.next
        newHead = head
        newHead.next = None

        while nxt != None:
            temp = nxt
            nxt = nxt.next
            temp.next = newHead
            newHead = temp

        return newHead