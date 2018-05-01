class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        k = total_len // 2
        if total_len % 2 == 0:
            return (self.findKth(nums1, nums2, k) + self.findKth(nums1, nums2, k + 1)) / 2.0
        return self.findKth(nums1, nums2, k + 1) * 1.0

    def findKth(self, nums1, nums2, kth):
        """
        find kth element of two sorted list
        """
        if kth > len(nums1) + len(nums2):
            raise ValueError('kth should be lower than the total length of nums1 and nums2')
        l1 = l2 = 0
        while True:
            len1 = len(nums1) - l1
            len2 = len(nums2) - l2
            # base cases
            if len1 <= 0:
                return nums2[l2 + kth - 1]
            if len2 <= 0:
                return nums1[l1 + kth - 1]
            if kth == 1:
                return min(nums1[l1], nums2[l2])
            # swap
            if len1 > len2:
                len1, len2 = len2, len1
                nums1, nums2 = nums2, nums1
                l1, l2 = l2, l1
            # loop condition
            c1 = min(kth // 2, len1)
            c2 = kth - c1
            mid1, mid2 = nums1[l1 + c1 - 1], nums2[l2 + c2 - 1]

            if mid1 < mid2:
                l1 += c1
                kth -= c1
            elif mid1 > mid2:
                l2 += c2
                kth -= c2
            else:
                return mid1


if __name__ == '__main__':
    s = Solution()
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5, 'Wrong Answer!'
    assert s.findMedianSortedArrays([1, 2], [2]) == 2, 'Wrong Answer!'
