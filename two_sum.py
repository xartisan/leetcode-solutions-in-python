class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = {}
        for i, v in enumerate(nums):
            first = record.get(v, None)
            if first is None:
                record[target - v] = i
            else:
                return first, i
