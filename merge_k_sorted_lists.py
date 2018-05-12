import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        min_heap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(min_heap, (lst.val, i))

        dummy_node = ListNode(0)
        cur = dummy_node
        while min_heap:

            list_index = heapq.heappop(min_heap)[1]
            min_node = lists[list_index]
            cur.next = min_node
            cur = cur.next
            if min_node.next:
                lists[list_index] = min_node.next
                heapq.heappush(min_heap, (min_node.next.val, list_index))
        return dummy_node.next
