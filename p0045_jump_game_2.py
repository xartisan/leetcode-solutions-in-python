class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        can_reach_to = 0
        next_reach_to = 0
        steps = 0

        for i, num in enumerate(nums):
            if can_reach_to >= len(nums) - 1:
                break
            if i > can_reach_to:
                can_reach_to = next_reach_to
                steps += 1
            next_reach_to = max(next_reach_to, num + i)
        return steps
