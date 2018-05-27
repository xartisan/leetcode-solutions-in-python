class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)

        level = 0

        while level < length // 2:

            for i in range(level, length -level - 1):
                tmp = matrix[level][i]
                for x, y in [(i, -level -1), (-level - 1, -i - 1), (-i - 1, level), (level, i)]:
                    tmp, matrix[x][y] = matrix[x][y], tmp
            level += 1
            
        