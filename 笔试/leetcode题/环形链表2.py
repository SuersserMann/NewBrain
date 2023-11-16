# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dict = {}
        cur = head
        while cur:
            if cur in dict:
                return cur
            else:
                dict[cur] = cur.val
                cur = cur.next
        return None