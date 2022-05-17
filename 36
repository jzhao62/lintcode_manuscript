def reverse_between(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head;
        p1, p2 = dummy, head
        for _ in range(m-1):
            p1 = p1.next;
            p2 = p2.next;

        prev1, prev2 = p1, p2
        p1=p1.next;
        p2=p2.next;

        for _ in range(n-m):
            new_p = p2.next;
            p2.next= p1
            p1 = p2;
            p2 = new_p
        

        prev1.next = p1
        prev2.next= p2

        return dummy.next;
