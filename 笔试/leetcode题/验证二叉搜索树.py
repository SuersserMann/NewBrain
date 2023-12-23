# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
# def isValidBST(self, root):
#     def travel(node, l, r):
#         if not node:
#             return True
#         if l < node.val < r:
#             a = travel(node.left, l, node.val)
#             b = travel(node.right, node.val, r)
#             return a and b
#         else:
#             return False
#
#     return travel(root, float("-inf"), float("inf"))
# Definition for a binary tree node.
class Solution:
    def __init__(self):
        self.pre = float('-inf')

    def isValidBST(self, root):

        if not root:
            return True

        if not self.isValidBST(root.left) or root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)
