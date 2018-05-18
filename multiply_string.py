class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # reverse
        num1 = num1[::-1]
        num2 = num2[::-1]
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        record = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            carry = 0
            num_i = int(num1[i])
            for j in range(len(num2)):
                s = num_i * int(num2[j]) + carry
                carry, r = divmod(s, 10)
                carry2, r = divmod(r + record[i + j], 10)
                record[i + j] = r
                record[i + j + 1] += carry2
            record[i + j + 1] += carry
        return ''.join(str(x) for x in reversed(record)).lstrip('0') or '0'