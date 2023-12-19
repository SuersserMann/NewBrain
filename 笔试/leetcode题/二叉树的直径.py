# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node:
                L = dfs(node.left)
                R = dfs(node.right)
            else:
                return 0
            self.res = max(L + R + 1, self.res)
            return max(L, R)+1

        dfs(root)
        return self.res-1
