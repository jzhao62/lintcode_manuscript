"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


def display_node(node):
    while node:
        print('->', node.val, end='')
        node = node.next
    print('-> None')


def merge_nodes(node1, node2):
    dummy = ListNode(0)
    head = dummy;

    # display_node(dummy.next)
    # display_node(node1)
    # display_node(node2);
    # print('*****')

    while node1 and node2:
        if node1.val < node2.val:
            head.next = node1;
            node1 = node1.next;
        else:
            head.next = node2;
            node2 = node2.next;
        head = head.next;

    # display_node(dummy.next)
    # display_node(node1)
    # display_node(node2);
    # print('--------')

    if node1:
        head.next = node1;
        node1 = node1.next;
    if node2:
        head.next = node2;
        node2 = node2.next;

    return dummy.next;


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        if len(lists) == 0: return None;

        return self.merge_range_lists(lists, 0, len(lists) - 1)

    def merge_range_lists(self, lists, start, end):

        if start == end:
            return lists[start];

        display_node(lists[start])

        mid = (start + end) // 2;

        left_sorted = self.merge_range_lists(lists, start, mid);
        right_sorted = self.merge_range_lists(lists, mid + 1, end);

        return merge_nodes(left_sorted, right_sorted)