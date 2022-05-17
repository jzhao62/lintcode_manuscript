"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


# 如果不知道prev，按照正常的思维这题是无解的
# code 本身没有问题
class Solution:

    def deleteNode(self, node):
        dummy = ListNode(-1)
        dummy.next= node;
        prev_slow = dummy
        slow = node;
        fast = node

        while fast.next and fast.next.next:
            prev_slow = slow
            slow = slow.next;
            fast = fast.next.next;
        
        prev_slow.next = slow.next;

        return dummy.next;
