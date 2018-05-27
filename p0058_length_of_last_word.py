class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        rv = 0
        find = False
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalpha():
                rv += 1
                find = True
            elif find:
                break
        return rv
