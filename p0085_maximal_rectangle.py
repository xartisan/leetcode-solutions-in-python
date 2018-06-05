class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        max_area = 0
        num_cols = len(matrix[0])
        heights = [0] * (num_cols + 1)
        for row in matrix:
            stack = [-1]
            for i in range(num_cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, w * h)
                stack.append(i)
    
        return max_area
