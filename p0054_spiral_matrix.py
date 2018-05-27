class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rv = []
        # limit
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        # 0, 1, 2, 3 
        direction = 0

        row = col = 0
        while bottom <= top and left <= right:
            if direction == 0:
                if col > right:
                    col = right
                    row += 1
                    direction = 1
                    top += 1
                else:
                    rv.append(matrix[row][col])
                    col += 1
            elif direction == 1:
                if row > bottom:
                    row = bottom
                    col -= 1
                    direction = 2
                    right -= 1
                else:
                    rv.append(matrix[row][col])
                    row += 1
            elif direction == 2:
                if col < left:
                    col = left
                    row -= 1
                    direction = 3
                    bottom -= 1
                else:
                    rv.append(matrix[row][col])
                    col -= 1
            else:
                if row < top:
                    row = top
                    col += 1
                    direction = 0
                    left += 1
                else:
                    rv.append(matrix[row][col])
                    row -= 1
        return rv