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
                
        def to_string(q):
            rv = []
            for case in q:
                case_string = []
                for col in case:
                    row_string = '.' * col + 'Q' + '.' * (n - 1 - col)
                    case_string.append(row_string)
                rv.append(case_string)
            return rv

        return to_string(helper(n))
    
