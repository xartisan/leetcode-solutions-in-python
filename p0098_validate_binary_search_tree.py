# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def is_valid_rec(node, left, right):
            if node is None:
                return True
            v = node.val
            if not left < v < right:
                return False

            return is_valid_rec(node.left, left, v) and is_valid_rec(node.right, v, right)

        return is_valid_rec(root, float('-inf'), float('inf'))
