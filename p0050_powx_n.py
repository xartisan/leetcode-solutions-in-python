class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        sign = -1 if n < 0 else 1        
        n = abs(n)
        rv = 1

        while n > 0:
            if n & 1:
                rv *= x
            n >>= 1
            rv *= rv
        
        if sign == -1:
            rv /= 1
        return rv