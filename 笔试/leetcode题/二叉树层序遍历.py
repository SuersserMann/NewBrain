# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        path = []
        last = [root]
        cur = []
        if not root:
            return path
        else:
            path.append([root.val])
            while 1:
                for i in last:
                    root = i
                    if root.left:
                        cur.append(root.left)
                    if root.right:
                        cur.append(root.right)
                cur_val = [i.val for i in cur]
                if not cur:
                    return path
                path.append(cur_val)
                last = cur

                cur = []

        return path
