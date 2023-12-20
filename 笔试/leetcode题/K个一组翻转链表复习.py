class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        def reverse(h, t):
            pre = None
            cur = h
            n = None
            while pre != t:
                n = cur.next
                cur.next = pre
                pre = cur
                cur = n
            return h, t

        pre_v = dummy
        head_v = head
        tail_v = head_v
        while head_v:
            for i in range(k - 1):
                tail_v = tail_v.next
                if not tail_v:
                    return dummy.next
            n_h = tail_v.next
            h, t = reverse(head_v, tail_v)
            pre_v.next = t
            h.next = n_h

            pre_v = h
            head_v = n_h
            tail_v = n_h
        return dummy.next
