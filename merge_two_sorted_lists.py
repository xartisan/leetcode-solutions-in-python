# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        cur = dummy_node
        while l1 or l2:
            if not (l1 and l2):
                cur.next = l1 or l2
                break            
            head1, head2 = l1.val, l2.val
            if head1 < head2:
                cur.next = ListNode(head1)
                l1 = l1.next
            else:
                cur.next = ListNode(head2)
                l2 = l2.next
            cur = cur.next

        return dummy_node.next
