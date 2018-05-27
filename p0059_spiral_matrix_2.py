class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rv = [[0] * n for _ in range(n)]

        row = col = 0
        left = top = 0
        right = bottom = n - 1
        row_step, col_step = 0, 1
        for i in range(1, n * n + 1):
            # check for out of boundary case
            if col < left or col > right or row < top or row > bottom:
                if col_step == 1:
                    col = right
                    row += 1
                    top += 1
                    row_step, col_step = 1, 0
                elif row_step == 1:
                    row = bottom
                    col -= 1
                    right -= 1
                    row_step, col_step = 0, -1
                elif col_step == -1:
                    col = left
                    row -= 1
                    bottom -= 1
                    row_step, col_step = -1, 0
                else:
                    row = top
                    col += 1
                    left += 1
                    row_step, col_step = 0, 1

            rv[row][col] = i
            row += row_step
            col += col_step

        return rv