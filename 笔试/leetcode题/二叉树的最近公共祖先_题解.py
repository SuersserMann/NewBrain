# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if not node:
                return None
            if node==p or node==q:
                return node
            x = dfs(node.left)
            y = dfs(node.right)

            if x and y:
                return node
            if x and not y:
                return x
            if y and not x:
                return y
            else:
                return None
        return dfs(root)

root = TreeNode(3)
p = TreeNode(5)
root.left = p
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
q = TreeNode(4)
root.left.right.right = q

s = Solution()
print(s.lowestCommonAncestor(root, p, q))