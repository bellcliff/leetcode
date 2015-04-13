
'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        ns = []
        subns = [root]
        subvs = [root.val]
        reverse = False
        while 1:
            ns.append(subvs)
            reverse = not reverse
            subns, subvs = self.sub(subns, reverse)
            if len(subns) is 0:
                break
        return ns


    def sub(self, nodes, reverse):  # sub and reverse
        ns, vs = [], []
        for node in nodes:
            for n in [node.left, node.right]:
                if n:
                    ns.append(n)
                    vs.append(n.val)
        if reverse:
            vs.reverse()
        return ns, vs
