class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        rv = []
        Solution._permuteUniqueHelper([], nums, rv)
        return rv
        
    @staticmethod
    def _permuteUniqueHelper(acc, lefts, rv):
        if not lefts or all(num == lefts[0] for num in lefts):
            acc.extend(lefts)
            rv.append(acc)
            return
        
        # less than all of lefts
        last_num = lefts[0] - 1 
        
        for i, num in enumerate(lefts):
            if num == last_num:
                continue
            new_acc = acc[:] 
            new_acc.append(num)
            new_lefts = lefts[:i] + lefts[i + 1:]
            Solution._permuteUniqueHelper(new_acc, new_lefts, rv)
            last_num = num