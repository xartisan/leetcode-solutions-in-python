class Solution:

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        assert isinstance(s, str) and isinstance(p, str), 'Type of arguments should be str'
        record = [[False] * len(p) for _ in range(len(s))]
        visited = [[False] * len(p) for _ in range(len(s))]
        return Solution._isMatcherHelper(s, 0, p, 0, record, visited)

    @staticmethod
    def _isMatcherHelper(s, si, p, pi, record, visited):
        # base cases
        if pi == len(p):
            return si == len(s)
        if (si == len(s)):
            return Solution._canMatchEmpty(p, pi)
        if visited[si][pi]:
            return record[si][pi]

        s_char = s[si]
        p_char = p[pi]

        if pi + 1 < len(p) and p[pi + 1] == '*':
            match = Solution._isMatcherHelper(
                s, si, p, pi + 2, record,
                visited) or (Solution._charMatch(s_char, p_char)
                             and Solution._isMatcherHelper(s, si + 1, p, pi, record, visited))
        else:
            match = Solution._charMatch(s_char, p_char) and Solution._isMatcherHelper(
                s, si + 1, p, pi + 1, record, visited)

        visited[si][pi] = True
        record[si][pi] = match
        return match

    @staticmethod
    def _canMatchEmpty(p, pi):
        while pi < len(p):
            while pi < len(p) and p[pi] == '*':
                pi += 1
            if pi > len(p):
                return False
            if pi + 1 >= len(p) or p[pi + 1] != '*':
                return False
            pi += 2
        return True

    @staticmethod
    def _charMatch(s_char, p_char):
        return s_char == p_char or p_char == '.'
