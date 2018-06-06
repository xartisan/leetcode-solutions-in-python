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
        def is_valid(l_bound, r_bound, node):
            if node.left:
                if node.left.val >= node.val:
                    return False
                if node.left.val <= l_bound:
                    return False
            if node.right:
                if node.right.val <= node.val:
                    return False
                if node.right.val >= r_bound:
                    return False
            return True
            
        stack = []
        stack.append((float('-inf'), float('inf'), root))
        while stack:
            l_bound, r_bound, node = stack.pop()
            if node is None:
                continue
            if not is_valid(l_bound, r_bound, node):
                return False
            stack.append((node.val, r_bound, node.right))
            stack.append((l_bound, node.val, node.left))
        return True
