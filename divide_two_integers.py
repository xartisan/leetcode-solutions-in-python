class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        div = divisor
        rv = 0
        step = 1 if positive else -1
        q = step
        while dividend >= divisor:
                dividend -= div
                rv += q
                q += q
                div += div
                if dividend < div:
                    div = divisor
                    q = step
        return min(max(-2147483648, rv), 2147483647)