class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def is_valid(i, case):
            for row, col in enumerate(case):
                if col == i:
                    return False
                if abs(row - len(case)) == abs(col - i):
                    return False
            return True

        def helper(nth):
            if nth == 0:
                return [[]]
            prev_cases = helper(nth - 1)
            rv = []
            for case in prev_cases:
                for i in range(n):
                    if is_valid(i, case):
                        tmp = case[:]
                        tmp.append(i)
                        rv.append(tmp)
            return rv
                

        return len(helper(n))
