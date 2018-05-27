class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        g = {}

        for s in strs:
            g.setdefault(''.join(sorted(s)), []).append(s)
        
        rv = []
        for gp in g.values():
            rv.append(gp)
        return rv