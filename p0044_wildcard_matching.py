class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        si = pi = 0
        # backtrack index
        bsi = bpi = -1    
        while si < len(s):
            
            if pi < len(p) and (p[pi] == s[si] or p[pi] == '?'):
                si += 1
                pi += 1
            elif pi < len(p) and p[pi] == '*':
                pi += 1
                bpi = pi
                bsi = si
            elif bpi != -1:
                bsi += 1
                si, pi = bsi, bpi
            else:
                return False
        # can match empty
        while pi < len(p):
            if p[pi] != '*':
                return False
            pi += 1
        return True