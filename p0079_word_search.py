class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        num_rows = len(board)
        num_cols = len(board[0])

        visited = [[False] * num_cols for _ in range(num_rows)]

        def neighbors(row, col, elem):
            ns = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
            rv = []
            for r, c in ns:
                if 0 <= r < num_rows and 0 <= c < num_cols and board[r][c] == elem and not visited[r][c]:
                    rv.append((r, c))
            return rv

        def dfs(row, col, word_index):
            visited[row][col] = True
            if word_index == len(word) - 1:
                return True

            char = word[word_index + 1]
            ns = neighbors(row, col, char)
            for next_row, next_col in ns:
                if dfs(next_row, next_col, word_index + 1):
                    return True
            visited[row][col] = False
            return False
        head = word[0]
        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == head:
                    if dfs(row, col, 0):
                        return True
        
        return False

