class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        record = [[-1] * (n + 1) for _ in range(n + 1)]


        def _trees(start=1, end=n):
            if start >= end:
                return 1
            x = record[start][end]
            if x != -1:
                return x
            r = 0            
            for i in range(start, end + 1):
                l = _trees(start, i - 1)
                rr = _trees(i + 1, end)
                r += l * rr
            record[start][end] = r
            return r
        
        return _trees()
