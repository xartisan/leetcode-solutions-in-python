class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s

        rv = [[] for i in range(numRows)]
        index, step = 0, 1
        for c in s:
            rv[index].append(c)
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step
        return ''.join(''.join(row) for row in rv)
