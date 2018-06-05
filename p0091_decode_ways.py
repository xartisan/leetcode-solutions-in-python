class Solution:
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        
        r1 = r2 = 1
        for i in range(1, len(s)):
            r0 = 0
            if s[i] != '0':
                r0 += r1
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                r0 += r2
            
            r1, r2 = r0, r1
        return r1