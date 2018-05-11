class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        reversed_value = 0
        xx = x
        while xx != 0:
            xx, r = divmod(xx, 10)
            reversed_value = reversed_value * 10 + r
           
        return reversed_value == x 