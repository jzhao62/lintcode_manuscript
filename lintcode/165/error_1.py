from data_structures.ListNode import  *
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

            # 29 -> 36 逻辑性错误
            if p1.val <= p2.val:
                p.next = p1
            else:
                p.next = p2

            p1 = p1.next
            p2 = p2.next



        # 为什么不可以用 while? 因为这里值更新了p2, 却没有更新P， 这样就可以了

        # while p1:
        #     p.next = p1
        #     p1 = p1.next
        #     p = p.next

        while p1:
            p.next = p1
            p1 = p1.next
        while p2:
            p.next = p2
            p2 = p2.next

        return dummy.next



l1 = serialize_to_listNode('null')
l2 = serialize_to_listNode('0->3->3->null')

result_node = Solution().merge_two_lists(l1, l2)

print(result_node)