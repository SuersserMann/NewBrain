# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur1=headA
        cur2=headB
        dict={}
        while cur1:
            dict[cur1]=cur1
            cur1=cur1.next
        while cur2:
            if cur2 in dict:
                return cur2
            cur2=cur2.next
        return None