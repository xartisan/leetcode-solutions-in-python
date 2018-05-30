class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # use first row and first col to record
        first_row = first_col = False
        for i in range(num_cols):
            if matrix[0][i] == 0:
                first_row = True
                break
        for i in range(num_rows):
            if matrix[i][0] == 0:
                first_col = True
                break
        for row in range(1, num_rows):
            for col in range(1, num_cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = matrix[row][0] = 0
        for row in range(1, num_rows):
            for col in range(1, num_cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        if first_row:
            for col in range(0, num_cols):
                matrix[0][col] = 0
            
        if first_col:
            for row in range(0, num_rows):
                matrix[row][0] = 0
