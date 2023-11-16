# Definition for a binary tree node.
import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """

        res = []

        def preorder(node):
            if not node:
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        cur = root
        for i in res[1:]:
            cur.left = None
            cur.right = TreeNode(i)
            cur = cur.right
        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

# Flatten the tree
s = Solution()
current = s.flatten(root)

# Print the flattened tree for testing

while current:
    print(current.val, end=" ")
    current = current.right
