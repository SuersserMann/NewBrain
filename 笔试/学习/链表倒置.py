class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
cur = node1
while cur:
    print(cur.val)
    cur = cur.next


def reverse(node):
    if node.val is None:
        return None
    elif node.next.val is None:
        return node
    else:
        pre = node
        cur = node.next
        pre.next = None
        while cur:
            node_next = cur.next
            cur.next = pre
            pre = cur
            cur = node_next
        return pre


x = reverse(node1)
while x:
    print(x.val)
    x = x.next
