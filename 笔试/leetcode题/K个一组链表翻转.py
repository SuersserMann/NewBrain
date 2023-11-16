class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        def reverse(head, tail):
            pre = 0
            cur = head
            while pre != tail:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return tail, head

        start = ListNode(0)
        start.next = head
        pre = start

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return start.next
            next = tail.next
            head, tail = reverse(head, tail)

            pre.next = head
            tail.next = next
            pre = tail
            head = tail.next
        return start.next
