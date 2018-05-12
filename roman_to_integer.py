class Solution:
    def romanToInt(self, roman_str):
        """
        :type s: str
        :rtype: int
        """
        if not roman_str:
            return 0
        roman_str_i = 0
        values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        rv = 0
        i = len(symbols) - 1
        while i >= 0 and roman_str_i < len(roman_str):
            s = symbols[i]
            v = values[i]
            symbol_len = len(s)
            while roman_str.startswith(s, roman_str_i):
                roman_str_i += symbol_len
                rv += v
            i -= 1
        return rv
