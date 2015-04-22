# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValid(root)
    
    def isValid(self, node, _min=None, _max=None):
        if node is None:
            return True
        if _min is not None and node.val <= _min:
            return False
        if _max is not None and node.val >= _max:
            return False
        if node.left is not None and not self.isValid(node.left, _min, node.val):
            return False
        if node.right is not None and not self.isValid(node.right, node.val, _max):
            return False
        return True