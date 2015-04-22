# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None or (root.left is None or root.right is None):
            return
        nodes = self.c([root])
        while len(nodes) > 1:
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i+1]
            nodes = self.c(nodes)
        return

    def c(self, ns):
        ncs = []
        for n in ns:
            if n.left is not None:
                ncs.append(n.left)
            if n.right is not None:
                ncs.append(n.right)
        return ncs
