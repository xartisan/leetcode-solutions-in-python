from collections import Counter

class Solution:
    def isScramble(self, s1, s2):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-pla
        ce instead.
        """
        if s1 == s2:
            return True
        counter1 = Counter(s1)
        counter2 = Counter(s2)
        if counter1 != counter2:
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) \
                or self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:len(s2) - i]):
                return True
        return False
