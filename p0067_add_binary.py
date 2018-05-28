class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        from itertools import zip_longest
        carry = 0
        rv = []
        table = {
            '1': 1,
            '0': 0
        }
        for x, y in zip_longest(reversed(a), reversed(b), fillvalue='0'):
            carry, d = divmod(carry + table[x] + table[y], 2)
            rv.append(str(d))
        if carry != 0:
            rv.append(str(carry))
        return ''.join(reversed(rv))
        