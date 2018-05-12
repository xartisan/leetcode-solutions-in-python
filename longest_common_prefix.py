class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        rv = ''
        for t in zip(*strs):
            first_c = t[0]
            for c in t:
                if c != first_c:
                    return rv
            rv += c

        return rv
