# https://leetcode.com/problems/copy-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        copyNodes = []
        originalNodes = dict()
        originalHead = head
        sentinel = Node(0)
        tail = sentinel
        nodeNumber = 0

        while head:
            originalNodes[head] = nodeNumber
            tail.next = Node(head.val, head.next)
            tail = tail.next
            head = head.next
            copyNodes.append(tail)
            nodeNumber += 1

        head = originalHead
        tail = sentinel.next

        while tail:
            if head.random:
                tail.random = copyNodes[originalNodes[head.random]]
            tail = tail.next
            head = head.next

        return sentinel.next