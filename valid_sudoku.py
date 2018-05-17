class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        empty = '.'

        for row in range(9):
            row_collisions = set()
            column_collisions = set()
            sub_sudoku_collisions = set()
            for col in range(9):
                row_elem = board[row][col]
                col_elem = board[col][row]
                sub_sudoku_elem = board[row // 3 * 3 + col // 3][row % 3 * 3 + col % 3]

                if row_elem in row_collisions or col_elem in column_collisions or \
                    sub_sudoku_elem in sub_sudoku_collisions:
                    return False
                if row_elem != empty:
                    row_collisions.add(row_elem)
                if col_elem != empty:
                    column_collisions.add(col_elem)
                if sub_sudoku_elem != empty:
                    sub_sudoku_collisions.add(sub_sudoku_elem)
        return True

