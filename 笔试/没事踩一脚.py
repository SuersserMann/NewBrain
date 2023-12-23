class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


dummy = ListNode(1)
cur = dummy
cur.next = ListNode(2)
print(dummy.next.val)
