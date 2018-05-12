class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

        i = 12
        rv = []
        while i >= 0 and num > 0:
            v = values[i]
            if num >= v:
                s = symbols[i]
                q, num = divmod(num, v)
                rv.append(s * q)
            i -= 1
        return ''.join(rv)
