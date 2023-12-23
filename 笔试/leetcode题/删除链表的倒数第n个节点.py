class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 快慢指针
    # def removeNthFromEnd(self, head, n):
    #     pre = ListNode(0)
    #     dummy = pre
    #     pre.next = head
    #     count = 0
    #     start = head
    #     while start:
    #         count += 1
    #         start = start.next
    #     for i in range(count - n):
    #         pre = pre.next
    #     cur = pre.next.next
    #     pre.next = cur
    #     return dummy.next

    def removeNthFromEnd(self, head, n):
        pre = ListNode(0)
        dummy = pre
        pre.next = head
        cur = pre
        for i in range(n + 1):
            cur = cur.next
        while cur:
            pre = pre.next
            cur = cur.next
        inter = pre.next.next
        pre.next=inter
        return dummy.next


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
new_head = a.removeNthFromEnd(a1, 2)
cur2 = new_head
while cur2:
    print(cur2.val)
    cur2 = cur2.next
