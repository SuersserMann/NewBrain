class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(left - 1):
            pre = pre.next
        tail = pre
        pree=pre
        for i in range(right - left + 1):
            tail = tail.next

        after = tail.next
        start = pre.next
        cur = start

        while pre != tail:
            next=cur.next
            cur.next = pre
            pre = cur
            cur = next
        start.next = after
        pree.next = tail
        return dummy.next
