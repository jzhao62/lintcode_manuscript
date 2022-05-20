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


input = "1->2->1->3->3->5->6->3->null"

head = serialize_to_listNode(input)

print(head)
