class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rv = []
        Solution._permuteHelper([], nums, rv)

        return rv

    @staticmethod
    def _permuteHelper(acc, lefts, rv):
        if not lefts:
            rv.append(acc)
            return
        
        for i, num in enumerate(lefts):
            new_lefts = lefts[:i] + lefts[i + 1:]
            new_acc = acc[:]
            new_acc.append(num)
            Solution._permuteHelper(new_acc, new_lefts, rv)
            
        