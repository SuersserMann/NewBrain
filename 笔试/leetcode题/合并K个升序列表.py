# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return
        elif len(lists) < 2:
            return lists[0]
        else:
            dummy = lists[0]
            pre = ListNode(0)
            last = pre
            for i in range(1, len(lists)):
                pre = last
                cur = dummy
                after = lists[i]
                if dummy and after and dummy.val >= after.val:
                    dummy = after
                elif after and not dummy:
                    dummy = after
                while cur and after:
                    if cur.val < after.val:
                        pre.next = cur
                        pre = cur
                        cur = cur.next
                    else:
                        pre.next = after
                        pre = after
                        after = after.next
                while cur:
                    pre.next = cur
                    pre = cur
                    cur = cur.next
                while after:
                    pre.next = after
                    pre = after
                    after = after.next
        x = dummy
        while x:
            print(x.val)
            x = x.next
        return dummy


list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
s = Solution()
print(s.mergeKLists([list1, list2, list3]))
