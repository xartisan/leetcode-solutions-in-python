class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row_len = len(obstacleGrid)
        col_len = len(obstacleGrid[0])

        paths_count_from = [[1] * col_len for _ in range(row_len)]
        for col in range(col_len - 1, -1, -1):
            if obstacleGrid[row_len - 1][col] == 1:
                paths_count_from[row_len - 1][col] = 0
            elif col < col_len - 1:
                paths_count_from[row_len - 1][col] = paths_count_from[row_len - 1][col + 1]
        
        for row in range(row_len - 1, -1, -1):
            if obstacleGrid[row][col_len - 1] == 1:
                paths_count_from[row][col_len - 1] = 0
            elif row < row_len - 1:
                paths_count_from[row][col_len - 1] = paths_count_from[row + 1][col_len - 1]

        for row in range(row_len - 2, -1, -1):
            for col in range(col_len - 2, -1, -1):
                if obstacleGrid[row][col] == 1:
                    paths_count_from[row][col] = 0
                else:
                    paths_count_from[row][col] = paths_count_from[row][col + 1] + paths_count_from[row + 1][col]
        return paths_count_from[0][0]