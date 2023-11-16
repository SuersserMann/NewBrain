# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        def forward(root, depth):
            if not root:
                return depth-1
            l = forward(root.left, depth + 1)
            r = forward(root.right, depth + 1)
            return max(l, r)
        return forward(root,1)
