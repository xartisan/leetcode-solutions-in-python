class Solution:

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        s = str.strip()
        if not s:
            return 0
        flag = 1
        if s.startswith(('+', '-')):
            if s.startswith('-'):
                flag = -1
            s = s[1:]

        if not s or not s[0].isdigit():
            return 0
        rv = 0
        for c in s:
            if not c.isdigit():
                break
            rv = rv * 10 + (ord(c) - ord('0'))
        rv *= flag
        if rv < INT_MIN:
            rv = INT_MIN
        elif rv > INT_MAX:
            rv = INT_MAX
        return rv
