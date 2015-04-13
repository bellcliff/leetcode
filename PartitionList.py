# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        h1 = ListNode(-1)
        h2 = ListNode(x)
        n = head
        a, b = h1, h2
        while n is not None:
            if n.val < x:
                a.next = ListNode(n.val)
                a = a.next
            else:
                b.next = ListNode(n.val)
                b = b.next
            n = n.next
        a.next = h2.next
        return h1.next
