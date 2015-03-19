# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        pass

    def mergeSort(self, head, pos):
        pass

    def mergeSplit(self, n1, iBegin, iEnd, n2):
        if iEnd - iBegin < 2:
            return
        iMiddle = (iEnd + iBegin) /2
        self.mergeSplit(n1, iBegin, iMiddle, n2)
        self.mergeSplit(n1, iMiddle, iEnd, n2)

    def mergeMerger(self, n1, iBegin, iMiddle, iEnd, n2):
        i0, i1 = iBegin, iMiddle
        for j in range(iBegin, iEnd):
            if i0 < iMiddle and (i1 > iEnd || A[i0] <= A[i1]):
                B[j] = A[i0]
                i0 = i0 + 1
            else:
                B[j] = A[i1]
                i1 = i1 + 1

    def sizeList(self, head):
        if head is None:
            return 0
        return self.sizeList(head.next) + 1

    def getTail(self, head):
        return head if head.next is None else self.getTail(head.next)

    def getNode(self, head, pos):
        if head is None:
            return None
        if pos is 0:
            return head
        return self.getNode(head.next, pos - 1)

    def switchNext(self, h1, h2):
        h1.next, h2.next = h2.next, h1.next

    def toNode(self, A):
        pnode = None
        hnode = None
        for a in A:
            node = ListNode(a)
            if pnode is not None:
                pnode.next = node
            else:
                hnode = node
            pnode = node
        return hnode

    def toList(self, head):
        A = []
        node = head
        while node is not None:
            A.append(node.val)
            node = node.next
        return A

    def printNode(self, head):
        print '->'.join(str(i) for i in self.toList(head))

s = Solution()
n = s.toNode([2,3,1,4,5])
s.printNode(n)
