class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keys = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        rv = []
        for d in digits:
            d = int(d)
            tmp = []
            for c in keys[d]:
                if rv:
                    tmp.extend(s + c for s in rv)
                else:
                    tmp.append(c)
            rv = tmp
        return rv
