class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        nth = 1
        digits = [1]

        while nth < n:
            nth_digits = []
            i = 0
            while i < len(digits):
                d = digits[i]
                count = 1
                j = i + 1
                while j < len(digits) and digits[j] == d:
                    count += 1
                    j += 1
                nth_digits.extend((count, d))
                i += count
            digits = nth_digits
            nth += 1
        return ''.join(str(i) for i in digits)