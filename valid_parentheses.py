from collections import deque
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match_table  = {
            '(': ')',
            '{': '}', 
            '[': ']'
        }
        d = deque()

        for c in s:
            if c in match_table:
                d.append(c)
            else:
                if not d:
                    return False
                last_c = d.pop()
                if match_table[last_c] != c:
                    return False
        return not bool(d)
