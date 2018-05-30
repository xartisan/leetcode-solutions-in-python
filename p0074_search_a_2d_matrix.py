class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        start, end = 0, num_rows - 1
        while start <= end:
            mid = (start + end) // 2
            mid_val = matrix[mid][0]
            if mid_val == target:
                return True
            elif mid_val < target:
                start = mid + 1
            else:
                end = mid - 1
        if end < 0:
            return False
        search_row = matrix[end]
        if target > search_row[-1]:
            return False
        start, end = 0, num_cols - 1
        while start <= end:
            mid = (start + end) // 2
            mid_val = search_row[mid]
            if mid_val == target:
                return True
            elif mid_val < target:
                start = mid + 1
            else:
                end = mid - 1
        return False