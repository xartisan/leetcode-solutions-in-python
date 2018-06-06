class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not (s1 and s2):
            return (s1 or s2) == s3
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        record = [[False] * (len(s1) + 1) for _ in range(len(s2) + 1)]

        record[0][0] = True


        for i in range(1, len(s1) + 1):
            record[0][i] = record[0][i - 1] and s1[i - 1] == s3[i - 1]
        
        for i in range(1, len(s2) + 1):
            record[i][0] = record[i - 1][0] and s2[i - 1] == s3[i - 1]
        
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                cond1 = record[j - 1][i] and s2[j - 1] == s3[i + j - 1]
                cond2 = record[j][i - 1] and s1[i - 1] == s3[i + j - 1]
                record[j][i] = cond1 or cond2
        
        return record[len(s2)][len(s1)]
        