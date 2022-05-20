from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:

        p1, p2 = l1, l2
        dummy = ListNode(-1)
        p = dummy

        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next

            else:
                p.next = p2
                p2 = p2.next

            p = p.next

        if p1:
            p.next = p1
        if p2:
            p.next = p2

        return dummy.next