class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # inplace sort
        nums.sort()
        nums_len = len(nums)
        rv = []
        for i in range(0, len(nums) - 2):
            # avoid repeated number cases [-1, -1, -1, 2]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]

            first, last = i + 1, nums_len - 1
            while first < last:
                sum_val = nums[first] + nums[last]
                if sum_val == target:
                    rv.append([nums[i], nums[first], nums[last]])
                    # skip repeated numbers
                    while first < last and nums[first] == nums[first + 1]:
                        first += 1
                    while last > first and nums[last] == nums[last-1]:
                        last -= 1
                    first += 1
                    last -= 1
                elif sum_val < target:
                    first += 1
                else:
                    last -= 1
        return rv
