# https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.n = n
        self.sentinel = ListNode(0, head)

        def travrsalNode(node: ListNode):
            if not node.next:
                return

            travrsalNode(node.next)

            self.n -= 1
            if self.n == 0:
                node.next = node.next.next
                return self.sentinel.next

        travrsalNode(self.sentinel)

        return self.sentinel.next