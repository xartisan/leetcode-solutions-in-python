class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False
        # check for sign
        if s.startswith(('+', '-')):
            s = s[1:]
        if not s or not (s[0].isdigit() or s[0] == '.'):
            return False
        for i in range(len(s)):
            if not s[i].isdigit():
                break
        if s[i].isdigit():
            return True

        found_dot = False
        found_e = False
        # .
        if s[i] == '.':
            found_dot = True
        elif s[i] == 'e':
            found_e = True
        else:
            return False
        i += 1
        if i >= len(s) and found_e:
            return False
    
        found_sign = False
        while i < len(s):
            c = s[i]
            if c == '.':
                return False
            elif c == 'e':
                if found_e or i < 2:
                    return False
                found_e = True
            elif c in '+-':
                if not found_e or found_sign:
                    return False
                found_sign = True
            elif not c.isdigit():
                return False
            i += 1
        if not s[i - 1].isdigit() and not (i > 1 and s[i - 1] == '.'):
            return False
        return True
        