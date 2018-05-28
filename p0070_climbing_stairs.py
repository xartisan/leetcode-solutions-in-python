class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        record = [1] * (n + 1)

        for i in range(2, n + 1):
            count = record[i - 1]
            count += record[i - 2]
            record[i] = count
        return record[n]
        