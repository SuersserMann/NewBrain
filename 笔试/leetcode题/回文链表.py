# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        xx=list(reversed(res))
        return res == xx


s = Solution()
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(2)
head.next.next.next=ListNode(1)
print(s.isPalindrome(head))
