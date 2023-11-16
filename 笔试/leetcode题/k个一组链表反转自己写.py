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

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            after = tail.next
            head, tail = reverse(head, tail)

            pre.next = head
            tail.next = after

            pre = tail
            head = tail.next
        return dummy.next
