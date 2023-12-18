# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        res = []
        stack = {}

        def dfs(root, deepth):
            if not root:
                return
            if deepth not in stack:
                res.append(root.val)
                stack[deepth] = deepth
            dfs(root.right, deepth + 1)
            dfs(root.left, deepth + 1)

        dfs(root, 0)
        return res
