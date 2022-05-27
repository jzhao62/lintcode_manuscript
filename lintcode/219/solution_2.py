from lintcode import (
    ListNode,
)


class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """

    def insert_node(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-float('inf'))
        dummy.next = head;
        p = dummy;

        while p.next and p.next.val < val:
            p = p.next;

        tmp = ListNode(val)

        p_ = p.next;
        p.next = tmp;
        tmp.next = p_

        return dummy.next;


head = ListNode.serialize_to_listNode('1->4->6->8->null')

head = Solution().insert_node(head, 5)

print(head)
