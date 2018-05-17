class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        Solution._helper(board, 0, 0)

    @staticmethod
    def _helper(board, i, j):
        if i == 9: return True
        if j >= 9: return Solution._helper(board, i + 1, 0)
        if board[i][j] == '.':
            for n in range(1, 10):
                elem = str(n)
                if Solution.is_valid(board, i, j, elem):
                    board[i][j] = elem
                    if Solution._helper(board, i, j + 1):
                        return True
            board[i][j] = '.'
        else:
            return Solution._helper(board, i, j + 1)
        return False

    
    @staticmethod
    def is_valid(board, i, j, elem):
        # row check
        for col in range(9):
            if col != j and board[i][col] == elem:
                return False
        # col check
        for row in range(9):
            if row != i and board[row][j] == elem:
                return False
        # sub sudoku check
        row_start, col_start = i // 3 * 3, j // 3 * 3
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if row != i and col != j:
                    if board[row][col] == elem:
                        return False
        return True
