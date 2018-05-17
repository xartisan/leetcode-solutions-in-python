class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rv = []
        Solution._helper([], candidates, target, rv)
        return rv

    @staticmethod
    def _helper(acc, left, target, rv):
        if target == 0:
            if acc:
                rv.append(acc)
            return
        if target < 0 or (not left):
            return
        Solution._helper(acc + [left[0]], left, target - left[0], rv)
        Solution._helper(acc, left[1:], target, rv)
        