class Solution:
    def swapPairs(self, head):
        '''
        cursive
        '''
        if not head or not head.next:
            return head
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next

    def swapPairs2(self, head):
        '''
        non cursive
        '''
        if not head or not head.next:
            return head
        newhead = head.next
        p = None
        while True:
            ''' move '''
            a = head.next
            b = head
            ''' swap '''
            b.next = a.next
            a.next = b
            if p is not None:
                p.next = a
            p = b
            head = b.next
            if not head or not head.next:
                break
        return newhead

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        vals = [self.val]
        a = self
        while a.next:
            a = a.next
            vals.append(a.val)
        return str(vals)

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

print Solution().swapPairs2(a)
