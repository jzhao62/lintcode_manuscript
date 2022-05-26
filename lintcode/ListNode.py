class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def serialize_to_listNode(serialized_list_nodes):
    arrs = serialized_list_nodes.split('->')

    dummy = ListNode(-1)
    p = dummy
    for c in arrs:
        if c == 'null': continue
        p.next = ListNode(int(c))
        p = p.next

    return dummy.next
