# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        prev = first = second = None
        stack = []
        cur = root
        while stack or cur:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if prev is not None and prev.val >= cur.val:
                    if first is None:
                        first = prev
                    second = cur
                prev = cur
                cur = cur.right
        
        first.val, second.val = second.val, first.val