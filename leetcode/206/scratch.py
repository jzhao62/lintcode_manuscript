# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = head
        p = head

        if not head or not head.next:
            return head

        while p:

            if p == prev:
                p = p.next
                # initially cut the prev.next if the prev is the first element, otherwise it will be circle
                # we do not cut prev.next in next steps, as prev.next will be trainling reversed nodes
                prev.next = None

            new_p = p.next

            p.next = prev

            prev = p

            p = new_p

        return prev

