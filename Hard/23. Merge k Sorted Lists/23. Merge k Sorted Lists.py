# https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(left, right):
            if left > right:
                return None
            if left == right:
                return lists[left]

            mid = (left + right) // 2
            return self.merge2Lists(
                merge(left, mid), 
                merge(mid + 1, right))

        return merge(0, len(lists) - 1)


    def merge2Lists(self, list1, list2):
        sentinel = ListNode()
        curr = sentinel

        while list1 and list2:

            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        curr.next = list1 if list1 else list2

        return sentinel.next



# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         k = len(lists)

#         if k == 0:
#             return None
#         elif k == 1:
#             return lists[0]

#         k2 = k // 2

#         return self.merge2Lists(
#             self.mergeKLists(lists[:k2]), 
#             self.mergeKLists(lists[k2:])
#             )


#     def merge2Lists(self, list1, list2):
#         sentinel = ListNode()
#         curr = sentinel

#         while list1 and list2:

#             if list1.val < list2.val:
#                 curr.next = list1
#                 list1 = list1.next
#             else:
#                 curr.next = list2
#                 list2 = list2.next

#             curr = curr.next

#         curr.next = list1 if list1 else list2

#         return sentinel.next