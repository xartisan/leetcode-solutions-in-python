# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def tostring(self):
        l = [None]
        r = [None]
        if self.left:
            l = self.left.tostring()
        if self.right:
            r = self.right.tostring()
        rv = [self.val]
        rv.extend(l)
        rv.extend(r)
        return rv

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []

        record = [[None] * (n + 1) for _ in range(n + 1)]
        def gather_trees(start=1, end=n):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            t = record[start][end]            
            if t is not None:
                return t

            temp = []
            for i in range(start, end + 1):
                left = gather_trees(start, i - 1)
                right = gather_trees(i + 1, end)
                for l in left:
                    for r in right:
                        t = TreeNode(i)
                        t.left = l
                        t.right = r
                        temp.append(t)
            record[start][end] = temp
            return temp
        return gather_trees()