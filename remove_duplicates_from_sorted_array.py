class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end = -1
        last_n = None
        for n in nums:
            if n != last_n:
                end += 1
                nums[end] = n
            last_n = n
        return end + 1