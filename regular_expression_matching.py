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


class Solution2:

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        si = pi = 0
        # backtrack stack
        bstack = []
        visited = [[False] * len(p) for _ in range(len(s))]
        while si < len(s):
            # check for visited case
            #print(si, pi, visited, bstack)
            if pi < len(p) and visited[si][pi]:
                if bstack:
                    si, pi = bstack.pop()
                else:
                    return False
            elif pi < len(p) - 1 and p[pi + 1] == '*':
                if p[pi] == s[si] or p[pi] == '.':
                    bstack.append((si + 1, pi))
                pi += 2
            elif pi < len(p) and (s[si] == p[pi] or p[pi] == '.'):
                si += 1
                pi += 1
            elif bstack:
                if pi < len(p):
                    visited[si][pi] = True
                si, pi = bstack.pop()
            else:
                return False
        # can match empty
        # must be format of x*
        while pi < len(p):
            if pi < len(p) - 1 and p[pi + 1] == '*':
                pi += 2
                continue
            return False
        return True