# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head
        last_end = dummy_node
        end = head
        step = 1
        k_list = None
        k_list_last = None
        while end:
            if step == k:
                tail = end.next
                end.next = k_list
                k_list = end
                k_list_last.next = tail
                last_end.next = k_list
                last_end = k_list_last
                k_list = None
                end = tail
                step = 1
            else:
                if step == 1:
                    k_list_last = end

                tmp = end
                end = end.next
                tmp.next = k_list
                k_list = tmp

                step += 1
        acc = None
        if k_list is not None:
            while k_list:
                tail = k_list.next
                k_list.next = acc
                acc = k_list
                k_list = tail
            last_end.next = acc


        return dummy_node.next