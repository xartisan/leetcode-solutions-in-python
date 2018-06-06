# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = []
        stack.append((p, q))
        while stack:
            l, r = stack.pop()
            if l is r:
                continue
            if l is None or r is None or l.val != r.val:
                return False
            stack.append((l.left, r.left))
            stack.append((l.right, r.right))
        return True