class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            d = digits[i]
            carry, d = divmod(d + carry, 10)
            digits[i] = d
        if carry != 0:
            digits.insert(0, carry)
        return digits
