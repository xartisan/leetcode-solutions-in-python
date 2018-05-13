class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        end = -1
        for n in nums:
            if n != val:
                end += 1
                nums[end] = n
        
        return end + 1