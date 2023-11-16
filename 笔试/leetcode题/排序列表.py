# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import numpy as np


class Solution:
    def sortList(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        idx = np.argsort(res)
        cur = ListNode()
        pre=cur
        for i in idx:
            new = ListNode(res[i])
            pre.next = new
            pre = pre.next
        return cur.next


data = [-1, 5, 3, 4, 0]
head = ListNode(data[0])
current = head

# 创建链表
for value in data[1:]:
    current.next = ListNode(value)
    current = current.next
s = Solution()
aa = s.sortList(head)
while aa:
    print(aa.val)
    aa = aa.next
