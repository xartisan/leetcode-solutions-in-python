class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        can_reach_to = 0
        next_can_reach_to = 0

        for i, num in enumerate(nums):
            if i > can_reach_to:
                if next_can_reach_to >= i:
                    can_reach_to = next_can_reach_to
                else:
                    return False

            next_can_reach_to = max(next_can_reach_to, i + num)
            if next_can_reach_to >= len(nums) - 1:
                return True
        return True