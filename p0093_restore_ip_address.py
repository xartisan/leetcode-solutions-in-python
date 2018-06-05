class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(s):
            if not s or s.startswith('0') and len(s) > 1:
                return False
            return 0 <= int(s) <= 255
        rv = []
        def picker(acc='', index=0, counter=4):
            if counter == 0:
                if index == len(s):
                    rv.append(acc)
                return
            # early termination            
            if (len(s) - index) > counter * 3:
                return
            
            if index >= len(s):
                return

            next_range = min(index + 3, len(s)) 
            for i in range(index + 1, next_range + 1):
                sub = s[index:i]
                if is_valid(sub):
                    if index != 0:
                        sub = '.' + sub
                    picker(acc + sub, i, counter - 1)

        picker()
        return rv
