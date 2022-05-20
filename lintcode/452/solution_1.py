from data_structures.ListNode import *

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """

    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev, p = dummy, head
        while p:
            if p.val == val:
                p = p.next;
                prev.next = p
            else:
                p = p.next;
                prev = prev.next
        return dummy.next


head = serialize_to_listNode('1->2->3->3->4->5->3->null')

head = Solution().remove_elements(head, 3)

print(head)
