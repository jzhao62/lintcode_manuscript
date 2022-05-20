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
    @param head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head: ListNode) -> ListNode:
        tail = None

        p = head;

        while p:
            _p = p.next;
            p.next = tail;
            tail = p
            p = _p

        return tail

