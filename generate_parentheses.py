class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rv = []
        Solution._helper('', rv, 0, n, 2 * n)
        return rv
    # recursive thinking is ok
    @staticmethod
    def _helper(acc, rv, sign_value, left_lps, total_length):
        # base cases
        if sign_value > 0:
            return
        if left_lps == 0:
            rv.append(acc + ')' * (total_length - len(acc)))
            return
        # loop condition
        Solution._helper(acc + '(', rv, sign_value - 1, left_lps - 1, total_length)
        Solution._helper(acc + ')', rv, sign_value + 1, left_lps, total_length)
