from lintcode.ListNode import *

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """

    def insert_node(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-float('inf'))
        dummy.next = head;
        prev, p = dummy, head

        while p:
            if prev.val <= val and val <= p.val:
                tmp = ListNode(val)
                prev.next = tmp;
                tmp.next = p
                return dummy.next;
            else:
                prev = prev.next;
                p = p.next;

        tmp = ListNode(val)
        prev.next = tmp;
        tmp.next = p
        return dummy.next
