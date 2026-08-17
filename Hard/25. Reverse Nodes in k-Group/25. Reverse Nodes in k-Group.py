# https://leetcode.com/problems/reverse-nodes-in-k-group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        sentinel = ListNode(0, head)
        group_prev = sentinel

        while True:
            # Find the kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return sentinel.next

            # Reverse the group
            group_next = kth.next
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect previous part to reversed group
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp