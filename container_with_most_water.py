class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                max_area = max(height[left] * (right - left), max_area)
                left += 1
            else:
                max_area = max(height[right] * (right - left), max_area)
                right -= 1
        return max_area
