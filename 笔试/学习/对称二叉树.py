# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        res1 = []
        res2 = []

        def back_l(root, res):
            if not root:
                res.append(None)
                return
            res.append(root.val)
            back_l(root.left, res)
            back_l(root.right, res)

        def back_r(root, res):
            if not root:
                res.append(None)
                return
            res.append(root.val)
            back_r(root.right, res)
            back_r(root.left, res)

        back_l(root.left, res1)
        back_r(root.right, res2)
        return res1 == res2
