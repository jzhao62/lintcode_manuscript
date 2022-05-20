"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """

    def hasCycle(self, head):
        p1 = head;
        p2 = head;

        while p2 and p2.next:
            p1 = p1.next;
            p2 = p2.next.next;
            if p1 is p2:
                return True
        return False