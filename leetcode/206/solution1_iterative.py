# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        # a more simple method is just to set prev NULL in the beginning, compared with the scratch.py, the code is neater
        prev = None;

        p = head

        while p:
            new_p = p.next

            p.next = prev

            prev = p

            p = new_p

        return prev


