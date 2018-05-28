class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        paths_count_to = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                paths_count_to[row][col] = paths_count_to[row - 1][col] + paths_count_to[row][col - 1]
        
        return paths_count_to[m-1][n-1]