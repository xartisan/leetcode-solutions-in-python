class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rv = []

        def picker(acc, index):
            if index >= len(nums):
                rv.append(acc)
                return
            picker(acc, index + 1)
            picker(acc + [nums[index]], index + 1)
        picker([], 0)
        return rv
    
    def subsets_loop(self, nums):
        rv = [[]]

        for num in nums:
            rv += [item + [num] for item in rv]
        return rv

