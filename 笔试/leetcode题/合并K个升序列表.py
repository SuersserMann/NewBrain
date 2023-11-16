import notebook_shim.shim
import numpy as np


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        res = []
        for i in lists:
            j = i
            while j:
                res.append(j.val)
                j = next
        res.sort()
        cur = head = ListNode(0)
        for i in res:
            cur.next = ListNode(i)
            cur = cur.next
        return head.next
