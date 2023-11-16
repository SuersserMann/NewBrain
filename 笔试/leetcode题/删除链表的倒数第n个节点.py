class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        res = ListNode(0, head)
        pre = res
        cur = head
        # [1,2,3,4,5],n=3
        # []
        for i in range(n):
            cur = cur.next
        while cur:
            cur = cur.next
            pre = pre.next
        pre.next = pre.next.next
        return res.next


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a = Solution()
new_head = a.removeNthFromEnd(a1, 5)
cur2 = new_head
while cur2:
    print(cur2.val)
    cur2 = cur2.next
