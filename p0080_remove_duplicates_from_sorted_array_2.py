class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        last_num = None
        last_num_count = 0
        LIMIT = 2
        for i in range(0, len(nums)):
            num = nums[i]
            if num == last_num and last_num_count >= LIMIT:
                continue
            if num == last_num:
                last_num_count += 1
            else:
                last_num = num
                last_num_count = 1
            if idx < i:
                nums[idx], nums[i] = nums[i], nums[idx]
            idx += 1
        return idx


        
