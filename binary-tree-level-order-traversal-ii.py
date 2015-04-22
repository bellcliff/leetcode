# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        vals = {}
        self.travel(root, 0, vals)
        results = []
        for i in range(len(vals)-1, -1, -1):
            results.append(vals[i])
        return results
    
    def travel(self, node, level, vals):
        if node is None:
            return
        if level not in vals:
            vals[level] = []
        vals[level].append(node.val)
        for n in [node.left, node.right]:
            self.travel(n, level+1, vals)
