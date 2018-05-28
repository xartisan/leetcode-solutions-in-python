class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_row = len(grid)
        num_col = len(grid[0])

        record = [[1] * num_col for _ in range(num_row)]
        record[num_row-1][num_col-1] = grid[num_row-1][num_col-1]

        for col in range(num_col - 2, -1, 1):
            record[num_row-1][col] += record[num_row-1][col+1]

        for row in range(num_row - 2, -1, -1):
            record[row][num_col-1] += record[row + 1][num_col-1]

        for row in range(num_row - 2, -1, -1):
            for col in range(num_col - 2, -1, -1):
                record[row][col] += min(record[row + 1][col], record[row][col + 1])
        return record[0][0]
