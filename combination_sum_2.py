class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        rv = []
        Solution._helper([], candidates, 0, target, rv)
        return rv

    @staticmethod
    def _helper(acc, candidates, candidates_cursor, target, rv):
        if target == 0:
            if acc:
                rv.append(acc)
            return
        if target < 0 or candidates_cursor >= len(candidates):
            return
        elem = candidates[candidates_cursor]
        Solution._helper(acc + [elem], candidates, candidates_cursor + 1, target - elem, rv)
        
        i = candidates_cursor + 1
        while i < len(candidates) and candidates[i] == elem:
            i += 1
        
        Solution._helper(acc, candidates, i, target, rv)