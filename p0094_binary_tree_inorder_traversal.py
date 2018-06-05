from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rv = []
        d = deque()
        VISIT, PRINT = 0, 1
        d.append((VISIT, root))
        
        while d:
            x = d.popleft()
            op, node = x
            if node is None:
                continue
            if op == PRINT:
                rv.append(node.val)
            else:
                d.appendleft((VISIT, node.right))
                d.appendleft((PRINT, node))
                d.appendleft((VISIT, node.left))

        return rv
        