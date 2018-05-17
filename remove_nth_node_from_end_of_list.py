class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        # exchange time for space
        dummy_node = ListNode(0)
        dummy_node.next = head
        nth_node = head
        nth_node_prev = dummy_node
        cur = head
        while cur:
            print(cur.val)
            length += 1
            if length > 7:
                nth_node_prev = nth_node
                nth_node = nth_node.next
            cur = cur.next
        
        nth_node_prev.next = nth_node.next
        return dummy_node.next
        
