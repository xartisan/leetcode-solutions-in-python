# Definition for singly-linked list.
class ListNode:

    def __init__(self, x, next_node=None):
        self.val = x
        self.next = next_node

    def __repr__(self):
        rv = str(self.val)
        if self.next is not None:
            rv += ' -> ' + repr(self.next)
        return rv


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # dummy node
        dummy_node = ListNode(0)
        cur_node = dummy_node
        acc = 0
        while l1 is not None or l2 is not None:
            s = acc + (l1 or dummy_node).val + (l2 or dummy_node).val
            acc = 0
            if s >= 10:
                s, acc = s - 10, 1
            new_node = ListNode(s)
            cur_node.next = new_node
            cur_node = new_node

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if acc == 1:
            cur_node.next = ListNode(1)

        return dummy_node.next


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    print(l1)
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print(l2)
    s = Solution()
    rv = s.addTwoNumbers(l1, l2)
    print(rv)
    assert repr(rv) == '7 -> 0 -> 8', 'Wrong answer!'
