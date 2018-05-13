class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            match = True
            for k in range(i, i + len(needle)):
                if haystack[k] != needle[k - i]:
                    match = False
                    break
            if match:
                return i
        return -1