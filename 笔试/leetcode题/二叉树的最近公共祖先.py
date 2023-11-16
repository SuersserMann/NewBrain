class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = []

        def dfs(node, path):
            if not node:
                return
            if len(res) == 2:
                return
            if node not in path:
                path.append(node)
                if node == p or node == q:
                    res.append(path.copy())
                dfs(node.left, path)
                dfs(node.right, path)
                path.remove(node)

        dfs(root, [])
        path1 = res[0]
        path2 = res[1]
        m = min(len(path1), len(path2))
        if path1[m-1]==path2[m-1]:
            return path1[m-1]
        for i in range(m):
            if path1[i] != path2[i]:
                return path1[i - 1]



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
