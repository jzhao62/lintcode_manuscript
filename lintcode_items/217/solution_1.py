from lintcode.ListNode import *


class Solution:

    def remove_duplicates(self, head: ListNode) -> ListNode:
        visited = set()

        dummy = ListNode(-1)
        dummy.next = head;

        prev, p = dummy, head
        while p:
            if p.val in visited:
                prev.next = p.next
                p = p.next
            else:
                visited.add(p.val)
                prev = p
                p = p.next

        return dummy.next


input = "1->2->1->3->3->5->6->3->null"
head = serialize_to_listNode(input)

s = Solution()

output = s.remove_duplicates(head)
