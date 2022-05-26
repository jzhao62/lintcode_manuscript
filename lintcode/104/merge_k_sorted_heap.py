import heapq


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


ListNode.__lt__ = lambda x, y: (x.val < y.val)


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        if not lists:
            return None;

        dummy = ListNode(-1)

        head = dummy

        heap = []

        for node in lists:
            if node:
                heapq.heappush(heap, node)

        while heap:
            curr = heapq.heappop(heap)
            head.next = curr;
            head = head.next;
            if head.next:
                heapq.heappush(heap, head.next)
        return dummy.next


# what happens if the initial lists are not sorted ?
# it is too slow, is there any way to make it faster ?
# what is the time complexity