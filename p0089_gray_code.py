class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [(i >> 1) ^ i for i in range(2 ** n)]
        return result
