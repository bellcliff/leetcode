# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        h = ListNode(-1)
        h.next = head
        n1 = h
        n2 = h
        i = 0
        while i < n:
            i+=1
            n2 = n2.next
        while n2.next is not None:
            n1 = n1.next
            n2 = n2.next
        n1.next = n1.next.next
        return h.next
